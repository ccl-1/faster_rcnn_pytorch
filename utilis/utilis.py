import numpy as np
import torch
from torch.nn import functional as F
#  bbox2loc, loc2bbox, bbox_iou, AnchorTargetCreator, ProposalTargetCreator


def bbox2loc(src_bbox, dst_bbox):
    '''
        已知 源框 和 目标框 求出其位置偏差
    '''
    
    # 计算出源框中心点坐标
    width = src_bbox[:, 2] - src_bbox[:, 0]
    height = src_bbox[:, 3] - src_bbox[:, 1]
    ctr_x = src_bbox[:, 0] + 0.5 * width
    ctr_y = src_bbox[:, 1] + 0.5 * height


    # 计算出目标框中心点坐标
    base_width = dst_bbox[:, 2] - dst_bbox[:, 0]
    base_height = dst_bbox[:, 3] - dst_bbox[:, 1]
    base_ctr_x = dst_bbox[:, 0] + 0.5 * base_width
    base_ctr_y = dst_bbox[:, 1] + 0.5 * base_height


    # 求出最小的正数
    eps = np.finfo(height.dtype).eps
    # 将height,width与其比较保证全部是非负
    height = np.maximum(height, eps)
    width = np.maximum(width, eps)

    # 根据上面的公式二计算dx，dy，dh，dw
    dx = (base_ctr_x - ctr_x) / width
    dy = (base_ctr_y - ctr_y) / height
    dw = np.log(base_width / width)
    dh = np.log(base_height / height)

    # np.vstack按照行的顺序把数组给堆叠起来
    loc = np.vstack((dx, dy, dw, dh)).transpose()
    return loc



def loc2bbox(src_bbox,loc):

    '''
        已知源bbox和位置偏差dx,dy,dh,dw，求目标框 G
    '''
    # src_bbox：（R，4），R为bbox个数，4为左上角和右下角四个坐标
    if src_bbox.shape[0] == 0:
        return np.zeros((0, 4), dtype=loc.dtype)
    
    # 源目标（cx,cy,w,h） 原始proposal 对应位置（Px,Py,Pw,Ph）
    src_width = torch.unsqueeze(src_bbox[:, 2] - src_bbox[:, 0], -1) # Pw
    src_height = torch.unsqueeze(src_bbox[:, 3] - src_bbox[:, 1], -1) # Ph
    src_ctr_x = torch.unsqueeze(src_bbox[:, 0], -1) + 0.5 * src_width  # Px
    src_ctr_y = torch.unsqueeze(src_bbox[:, 1], -1) + 0.5 * src_height # Py

    # 位置偏差
    dx = loc[:, 0::4]
    dy = loc[:, 1::4]
    dw = loc[:, 2::4]
    dh = loc[:, 3::4]
    
    # RCNN中提出的边框回归：寻找原始proposal与近似目标框G之间的映射关系,得到回归后的目标框（Gx,Gy,Gh,Gw）
    # Gx = dx*Pw + Px;  Gy = dy*Ph + Py;  Gw = exp(dw) * Pw; Gh = exp(dh) * Ph
    ctr_x = dx * src_width + src_ctr_x      # Gx
    ctr_y = dy * src_height + src_ctr_y     # Gy
    w = torch.exp(dw) * src_width           # Gw
    h = torch.exp(dh) * src_height          # Gh

    # 由中心点转换为左上角和右下角坐标
    dst_bbox = torch.zeros_like(loc)
    dst_bbox[:, 0::4] = ctr_x - 0.5 * w # 从id=0 开始,step=4 取值
    dst_bbox[:, 1::4] = ctr_y - 0.5 * h
    dst_bbox[:, 2::4] = ctr_x + 0.5 * w
    dst_bbox[:, 3::4] = ctr_y + 0.5 * h

    return dst_bbox



def bbox_iou(bbox_a, bbox_b):
    '''
        求两个bbox的相交的 交并比,    也就是对a里每个bbox都分别和b里的每个bbox求iou (N,K)
    '''
    # 确保bbox第二维为bbox的四个坐标（ymin，xmin，ymax，xmax）
    if bbox_a.shape[1] != 4 or bbox_b.shape[1] != 4:
        raise IndexError
    
    # top left 左上角坐标最大值，为了利用numpy的广播性质，
    # bbox_a[:, None, :2].shape是(N,1,2)，bbox_b[:, :2].shape是(K,2),由numpy的广播性质，两个数组shape都变成(N,K,2)，
    tl = np.maximum(bbox_a[:, None, :2], bbox_b[:, :2])
    # bottom right 坐标最小值
    br = np.minimum(bbox_a[:, None, 2:], bbox_b[:, 2:])
    
    # 所有坐标轴上tl<br时，有相交区域
    area_i = np.prod(br - tl, axis=2) * (tl < br).all(axis=2) # bboxa 与 bboxb 相交区域的面积
    area_a = np.prod(bbox_a[:, 2:] - bbox_a[:, :2], axis=1)
    area_b = np.prod(bbox_b[:, 2:] - bbox_b[:, :2], axis=1)
    
    # 计算IOU
    return area_i / (area_a[:, None] + area_b - area_i) # （N,K）


# 从 {建议框预测结果} 获得 {真实框} 的过程被称作【解码】，而从 {真实框} 获得 {建议框预测结果} 的过程就是【编码】


class AnchorTargetCreator(object):
    '''
        作用： 将20000多候选框选出256进行二分类和所有anchor进行回归位置。生成训练要用的anchor(正负样本各128个)
        即：寻找 每一张【用于训练的图片】（ProposalTargetCreator 筛选生成）的每一个【真实框对应的先验框】（建议框预测结果），也就是 编码 过程
        具体流程：
            1） 对于每一个GT bbox，选择和它 交并比最大 的一个Anchor作为 正样本。
            2） 对于剩下的Anchor，从中选择和任意一个GT bbox交并比超过 【0.7】的Anchor作为 正样本，正样本数目不超过128个。
            3） 随机选择和GT bbox交并比小于【0.3】的Anchor作为 负样本，负样本和正样本的总数为 256
        计算 【分类损失】 使用的是【交叉熵损失】，而计算 【回归损失】 则使用了【SmoothL1Loss】，
        在计算 回归损失 的时候只计算 正样本（前景1）的损失，不计算负样本（背景0）的损失。
    '''
    def __init__(self, n_sample=256, pos_iou_thresh=0.7, neg_iou_thresh=0.3, pos_ratio=0.5):
        self.n_sample = n_sample
        self.pos_iou_thresh = pos_iou_thresh
        self.neg_iou_thresh = neg_iou_thresh
        self.pos_ratio = pos_ratio
    
    def __call__(self, bbox, anchor, img_size):
        argmax_ious, label = self._create_label(anchor, bbox)
        if (label>0).any():
            loc = bbox2loc(anchor, bbox[argmax_ious])
            return loc, label
        else:
            return np.zeros_like(anchor), label
    
    def _calc_ious(self, anchor, bbox):
        #----------------------------------------------#
        #   anchor和bbox的iou
        #   获得的ious的shape为[num_anchors, num_gt]
        #----------------------------------------------#
        ious = bbox_iou(anchor, bbox)
        
        if len(bbox)==0:
            return np.zeros(len(anchor), np.int32), np.zeros(len(anchor)), np.zeros(len(bbox))
        #---------------------------------------------------------#
        #   获得每一个先验框最对应的真实框  [num_anchors, ]
        #---------------------------------------------------------#
        argmax_ious = ious.argmax(axis=1)
        #---------------------------------------------------------#
        #   找出每一个先验框最对应的真实框的iou  [num_anchors, ]
        #---------------------------------------------------------#
        max_ious = np.max(ious, axis=1)
        
        #---------------------------------------------------------#
        #   获得每一个真实框最对应的先验框  [num_gt, ]
        #---------------------------------------------------------#
        gt_argmax_ious = ious.argmax(axis=0)
        
        #---------------------------------------------------------#
        #   保证每一个真实框都存在对应的先验框
        #---------------------------------------------------------#
        for i in range(len(gt_argmax_ious)):
            argmax_ious[gt_argmax_ious[i]] = i
        
        return argmax_ious, max_ious, gt_argmax_ious
    
    def _create_label(self, anchor, bbox):
        # ------------------------------------------ #
        #   1是正样本，0是负样本，-1忽略
        #   初始化的时候全部设置为-1
        # ------------------------------------------ #
        label = np.empty((len(anchor),), dtype=np.int32)
        label.fill(-1)
        
        # ------------------------------------------------------------------------ #
        #   argmax_ious为每个先验框对应的最大的真实框的序号         [num_anchors, ]
        #   max_ious为每个真实框对应的最大的真实框的iou             [num_anchors, ]
        #   gt_argmax_ious为每一个真实框对应的最大的先验框的序号    [num_gt, ]
        # ------------------------------------------------------------------------ #
        argmax_ious, max_ious, gt_argmax_ious = self._calc_ious(anchor, bbox)
        
        # ----------------------------------------------------- #
        #   如果小于门限值则设置为负样本
        #   如果大于门限值则设置为正样本
        #   每个真实框至少对应一个先验框
        # ----------------------------------------------------- #
        label[max_ious < self.neg_iou_thresh] = 0
        label[max_ious >= self.pos_iou_thresh] = 1
        if len(gt_argmax_ious)>0:
            label[gt_argmax_ious] = 1
        
        # ----------------------------------------------------- #
        #   判断正样本数量是否大于128，如果大于则限制在128
        # ----------------------------------------------------- #
        n_pos = int(self.pos_ratio * self.n_sample)
        pos_index = np.where(label == 1)[0]
        if len(pos_index) > n_pos:
            disable_index = np.random.choice(pos_index, size=(len(pos_index) - n_pos), replace=False)
            label[disable_index] = -1
        
        # ----------------------------------------------------- #
        #   平衡正负样本，保持总数量为256
        # ----------------------------------------------------- #
        n_neg = self.n_sample - np.sum(label == 1)
        neg_index = np.where(label == 0)[0]
        if len(neg_index) > n_neg:
            disable_index = np.random.choice(neg_index, size=(len(neg_index) - n_neg), replace=False)
            label[disable_index] = -1
        
        return argmax_ious, label




# ProposalCreator产生2000个ROIS，但是这些ROIS并不都用于训练，经过本ProposalTargetCreator的筛选产生 128个用于自身的训练
class ProposalTargetCreator(object):
    def __init__(self, n_sample=128, pos_ratio=0.5, pos_iou_thresh=0.5, neg_iou_thresh_high=0.5, neg_iou_thresh_low=0):
        self.n_sample = n_sample
        self.pos_ratio = pos_ratio
        self.pos_roi_per_image = np.round(self.n_sample * self.pos_ratio)
        self.pos_iou_thresh = pos_iou_thresh
        self.neg_iou_thresh_high = neg_iou_thresh_high
        self.neg_iou_thresh_low = neg_iou_thresh_low
    
    def __call__(self, roi, bbox, label, loc_normalize_mean=(0., 0., 0., 0.), loc_normalize_std=(0.1, 0.1, 0.2, 0.2)):
        roi = np.concatenate((roi.detach().cpu().numpy(), bbox), axis=0)
        # ----------------------------------------------------- #
        #   计算建议框和真实框的重合程度
        # ----------------------------------------------------- #
        iou = bbox_iou(roi, bbox)
        
        if len(bbox)==0:
            gt_assignment = np.zeros(len(roi), np.int32)
            max_iou = np.zeros(len(roi))
            gt_roi_label = np.zeros(len(roi))
        else:
            #---------------------------------------------------------#
            #   获得每一个建议框最对应的真实框  [num_roi, ]
            #---------------------------------------------------------#
            gt_assignment = iou.argmax(axis=1)
            #---------------------------------------------------------#
            #   获得每一个建议框最对应的真实框的iou  [num_roi, ]
            #---------------------------------------------------------#
            max_iou = iou.max(axis=1)
            
            #---------------------------------------------------------#
            #   真实框的标签要+1因为有背景的存在
            #---------------------------------------------------------#
            gt_roi_label = label[gt_assignment] + 1
        
        #----------------------------------------------------------------#
        #   满足建议框和真实框重合程度大于neg_iou_thresh_high的作为负样本
        #   将正样本的数量限制在self.pos_roi_per_image以内
        #----------------------------------------------------------------#
        pos_index = np.where(max_iou >= self.pos_iou_thresh)[0]
        pos_roi_per_this_image = int(min(self.pos_roi_per_image, pos_index.size))
        if pos_index.size > 0:
            pos_index = np.random.choice(pos_index, size=pos_roi_per_this_image, replace=False)
        
        #-----------------------------------------------------------------------------------------------------#
        #   满足建议框和真实框重合程度小于neg_iou_thresh_high大于neg_iou_thresh_low作为负样本
        #   将正样本的数量和负样本的数量的总和固定成self.n_sample
        #-----------------------------------------------------------------------------------------------------#
        neg_index = np.where((max_iou < self.neg_iou_thresh_high) & (max_iou >= self.neg_iou_thresh_low))[0]
        neg_roi_per_this_image = self.n_sample - pos_roi_per_this_image
        neg_roi_per_this_image = int(min(neg_roi_per_this_image, neg_index.size))
        if neg_index.size > 0:
            neg_index = np.random.choice(neg_index, size=neg_roi_per_this_image, replace=False)
        
        #---------------------------------------------------------#
        #   sample_roi      [n_sample, ]
        #   gt_roi_loc      [n_sample, 4]
        #   gt_roi_label    [n_sample, ]
        #---------------------------------------------------------#
        keep_index = np.append(pos_index, neg_index)
        
        sample_roi = roi[keep_index]
        if len(bbox)==0:
            return sample_roi, np.zeros_like(sample_roi), gt_roi_label[keep_index]
        
        gt_roi_loc = bbox2loc(sample_roi, bbox[gt_assignment[keep_index]])
        gt_roi_loc = ((gt_roi_loc - np.array(loc_normalize_mean, np.float32)) / np.array(loc_normalize_std, np.float32))
        
        gt_roi_label = gt_roi_label[keep_index]
        gt_roi_label[pos_roi_per_this_image:] = 0
        return sample_roi, gt_roi_loc, gt_roi_label












