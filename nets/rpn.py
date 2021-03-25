import torch
from torch import nn
from torch.nn import functional as F
# 导入 anchor的生成库
from utilis.anchors import generate_anchor_base,_enumerate_shifted_anchor
from utilis.utilis import loc2bbox
from torchvision.ops import nms
import numpy as np


class ProposalCreator():
    '''
    返回： 修正，nms之后的 ROIs
    RPN在自身训练的时候还会提供ROIs给Faster RCNN的ROI Head作为训练样本。RPN生成ROIs的过程就是ProposalCreator，
    具体流程如下:
        1) 对于每张图片，利用它的特征图，计算（大约20000个）Anchor属于前景的概率以及对应的位置参数。
        2) 选取概率较大的12000个Anchor。
        3) 利用回归的位置参数修正这12000个Anchor的位置，获得ROIs。
        4)利用非极大值抑制，选出概率最大的2000个ROIs。
    在推理阶段，为了提高处理速度，12000和2000分别变成了6000和300。并且这部分操作不需要反向传播， 可以利用numpy/tensor实现

    PS:生成的 RoI 仅仅区分了前景和背景，并没有区分出物体的具体类别。因此，RoIHead 就是对 RoI 进一步分类，并且调整矩形框的位置和大小，使得预测结果更精细。
    '''
    def __init__(self,mode,nms_thresh=0.7,n_train_pre_nms=3000,n_train_post_nms=300,
                n_test_pre_nms=3000,n_test_post_nms=300,min_size=16):
        self.mode = mode
        self.nms_thresh = nms_thresh
        self.n_train_pre_nms = n_train_pre_nms
        self.n_train_post_nms = n_train_post_nms
        self.n_test_pre_nms = n_test_pre_nms
        self.n_test_post_nms = n_test_post_nms
        self.min_size = min_size

    def __call__(self, loc, score, anchor, img_size, scale=1.):
        '''
            这 loc 和 score 是经过region_proposal_network中 经过1x1卷积分类和回归得到的。
        '''
        if self.mode == "training":
            n_pre_nms = self.n_train_pre_nms
            n_post_nms = self.n_train_post_nms
        else:
            n_pre_nms = self.n_test_pre_nms # 3000
            n_post_nms = self.n_test_post_nms # 经过NMS后有300个

        anchor = torch.from_numpy(anchor)
        if loc.is_cuda:
            anchor = anchor.cuda()
        #-----------------------------------#
        #   将RPN网络预测结果 转换为 近似GT的anchor(即rois)
        #-----------------------------------#
        roi = loc2bbox(anchor, loc)

        #-----------------------------------#
        #   防止建议框超出图像边缘，
        #   将rois的xmin,xmax限定在[0,W], ymin,ymax限定在[0,H]
        #-----------------------------------#
        roi[:, [0, 2]] = torch.clamp(roi[:, [0, 2]], min = 0, max = img_size[1])
        roi[:, [1, 3]] = torch.clamp(roi[:, [1, 3]], min = 0, max = img_size[0])

        #-----------------------------------#
        #   建议框的宽高的最小值不可以小于16
        #-----------------------------------#
        min_size = self.min_size * scale
        ws = roi[:, 2] - roi[:, 0]
        hs = roi[:, 3] - roi[:, 1]
        keep = torch.where((ws >= min_size) & (hs >= min_size))[0]
        roi = roi[keep, :]
        score = score[keep]

        #-----------------------------------#
        #   根据得分进行排序，取出建议框
        #-----------------------------------#
        order = torch.argsort(score, descending=True)
        if n_pre_nms > 0:
            order = order[:n_pre_nms]
        roi = roi[order, :]
        score = score[order]

        #-----------------------------------#
        #   对建议框进行非极大抑制
        #-----------------------------------#
        keep = nms(roi, score, self.nms_thresh)
        keep = keep[:n_post_nms]
        roi = roi[keep]
        return roi


class RegionProposalNetwork(nn.Module):
    def __init__(
            self, in_channels=512, mid_channels=512, ratios=[0.5, 1, 2],
            anchor_scales=[8, 16, 32], feat_stride=16,
            mode = "training",
    ):
        super(RegionProposalNetwork, self).__init__()
        self.feat_stride = feat_stride
        self.proposal_layer = ProposalCreator(mode)
        #-----------------------------------------#
        #   生成基础先验框，shape为[9, 4]
        #-----------------------------------------#
        self.anchor_base = generate_anchor_base(anchor_scales=anchor_scales, ratios=ratios)
        n_anchor = self.anchor_base.shape[0]
        
        #-----------------------------------------#
        #   先进行一个3x3的卷积，可理解为特征整合
        #-----------------------------------------#
        self.conv1 = nn.Conv2d(in_channels, mid_channels, 3, 1, 1)
        #-----------------------------------------#
        #   分类预测先验框内部是否包含物体
        #-----------------------------------------#
        self.score = nn.Conv2d(mid_channels, n_anchor * 2, 1, 1, 0)
        #-----------------------------------------#
        #   回归预测对先验框进行调整
        #-----------------------------------------#
        self.loc = nn.Conv2d(mid_channels, n_anchor * 4, 1, 1, 0)
        
        #--------------------------------------#
        #   对FPN的网络部分进行权值初始化
        #--------------------------------------#
        normal_init(self.conv1, 0, 0.01)
        normal_init(self.score, 0, 0.01)
        normal_init(self.loc, 0, 0.01)
    
    def forward(self, x, img_size, scale=1.):
        n, _, h, w = x.shape
        #-----------------------------------------#
        #   先进行一个3x3的卷积，可理解为特征整合
        #-----------------------------------------#
        x = F.relu(self.conv1(x))
        #-----------------------------------------#
        #   回归预测对先验框进行调整
        #-----------------------------------------#
        rpn_locs = self.loc(x)
        rpn_locs = rpn_locs.permute(0, 2, 3, 1).contiguous().view(n, -1, 4)
        #-----------------------------------------#
        #   分类预测先验框内部是否包含物体
        #-----------------------------------------#
        rpn_scores = self.score(x)
        rpn_scores = rpn_scores.permute(0, 2, 3, 1).contiguous().view(n, -1, 2)
        
        #--------------------------------------------------------------------------------------#
        #   进行softmax概率计算，每个先验框只有两个判别结果
        #   内部包含物体或者内部不包含物体，rpn_softmax_scores[:, :, 1]的内容为包含物体的概率
        #--------------------------------------------------------------------------------------#
        rpn_softmax_scores = F.softmax(rpn_scores, dim=-1)
        rpn_fg_scores = rpn_softmax_scores[:, :, 1].contiguous()
        rpn_fg_scores = rpn_fg_scores.view(n, -1)
        
        #------------------------------------------------------------------------------------------------#
        #   生成先验框，此时获得的anchor是布满网格点的，当输入图片为600,600,3的时候，shape为(12996, 4)
        #------------------------------------------------------------------------------------------------#
        anchor = _enumerate_shifted_anchor(np.array(self.anchor_base), self.feat_stride, h, w)
        
        rois = list()
        roi_indices = list()
        for i in range(n):
            roi = self.proposal_layer(rpn_locs[i], rpn_fg_scores[i], anchor, img_size, scale=scale)
            batch_index = i * torch.ones((len(roi),))
            rois.append(roi)
            roi_indices.append(batch_index)
        
        rois = torch.cat(rois, dim=0)
        roi_indices = torch.cat(roi_indices, dim=0)
        
        return rpn_locs, rpn_scores, rois, roi_indices, anchor



def normal_init(m, mean, stddev, truncated=False):
    if truncated:
        m.weight.data.normal_().fmod_(2).mul_(stddev).add_(mean)  # not a perfect approximation
    else:
        m.weight.data.normal_(mean, stddev)
        m.bias.data.zero_()
