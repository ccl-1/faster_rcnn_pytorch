import numpy as np

def generate_anchor_base(base_size=16, ratios=[0.5, 1, 2],
                        anchor_scales=[8, 16, 32]):
    ''' 生成 9个anchor 的坐标'''
    anchor_base = np.zeros((len(anchor_scales) * len(ratios), 4),dtype=np.float)
    
    for i in range(len(ratios)):
        for j in range(len(anchor_scales)):
            h = base_size * anchor_scales[j] * np.sqrt(ratios[i])
            w = base_size * anchor_scales[j] * np.sqrt(1. / ratios[i])

            index = i * len(anchor_scales) + j
            anchor_base[index, 0] = -h / 2.
            anchor_base[index, 1] = -w / 2.
            anchor_base[index, 2] = h / 2.
            anchor_base[index, 3] = w / 2.
    return anchor_base

def _enumerate_shifted_anchor(anchor_base,feat_stride,height,width):
    # https://my.oschina.net/u/4580321/blog/4358361
    """
        利用 anchor_base 生成所有对应feature map的 anchor 
        当前滑窗的中心在原像素空间的映射点称为anchor，以此anchor为中心，生成k个proposals。
        虽然 anchors 是基于卷积特征图定义的，但最终的 anchos 是相对于原始图片的. 
    """
    # 计算网格中心
    shift_x = np.arange(0, width * feat_stride, feat_stride)   # 横向偏移量（0，16，32，...）
    shift_y = np.arange(0, height * feat_stride, feat_stride)  # 纵向偏移量（0，16，32，...）
    # 矩阵找到映射在原图中的具体位置！
    shift_x, shift_y = np.meshgrid(shift_x, shift_y)  # shape=(38, 38)
    # meshgrid 输入网格点的横纵坐标列向量， 生成坐标矩阵。横坐标矩阵 X中的每个元素，与纵坐标矩阵 Y中对应位置元素，共同构成一个点的完整坐标。
    # shift_x = [[0，16，32，..],[0，16，32，..],[0，16，32，..]...],
    # shift_y = [[0，0，0，..],[16，16，16，..],[32，32，32，..]...],
    shift = np.stack((shift_x.ravel(),shift_y.ravel(),shift_x.ravel(),shift_y.ravel(),), axis=1)
    # 产生坐标偏移对(shift_x1,shift_y1,shift_x2,shift_y2),  相对anchor_base,    # shift.shape = (1444, 4)

    # 每个网格上的 9个先验框
    A = anchor_base.shape[0] # 9
    K = shift.shape[0] # 读取特征图中元素的总个数,anchor的总个数
    anchor = anchor_base.reshape((1, A, 4)) +  shift.reshape((K, 1, 4)) # anchor.shape = (1444, 9, 4)
    # 所有的先验框
    anchor = anchor.reshape((K * A, 4)).astype(np.float32)
    # 用基础的9个anchor的坐标分别和偏移量相加，最后得出了所有的anchor的坐标，
    # 一共K个特征点，每一个有A(9)个基本的anchor，所以最后reshape((K*A),4)的形式

    return anchor

if __name__ ==  "__main__":
    import matplotlib.pyplot as plt

    nine_anchors = generate_anchor_base()
    # print(nine_anchors)
    height, width, feat_stride = 38,38,16
    anchors_all = _enumerate_shifted_anchor(nine_anchors,feat_stride,height,width)
        
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ylim(-300,900)
    plt.xlim(-300,900)
    
    shift_x = np.arange(0, width * feat_stride, feat_stride)
    shift_y = np.arange(0, height * feat_stride, feat_stride)
    shift_x, shift_y = np.meshgrid(shift_x, shift_y)
    plt.scatter(shift_x,shift_y)

    #从这可以推断出，anchors_all 保存 [x1,y1,x2,y1] ......所有坐标信息
    box_widths = anchors_all[:,2]-anchors_all[:,0]   
    box_heights = anchors_all[:,3]-anchors_all[:,1]
    
    # 绘制一组anchor （一个anchor点对应的 9个框）
    for i in [108,109,110,111,112,113,114,115,116]:
        rect = plt.Rectangle([anchors_all[i, 0],anchors_all[i, 1]],box_widths[i],box_heights[i],color="r",fill=False)
        ax.add_patch(rect)
    
    plt.show()



# 大论文
#     弱小目标关键技术研究与应用
#     弱小目标在光学遥感方面的研究与应用