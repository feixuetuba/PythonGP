"""
PS 扭曲
"""
import cv2
import numpy as np

def displacement(bg, fg, scale_x, scale_y):
    """
    参考：https://github.com/karlphillip/GraphicsProgramming
    仿照PS的置换(dispace)效果，把fg置入bg中，这里用bg的灰度图作为参考
    :param bg:
    :param fg:
    :param scale_x: x的变换比例，对应PS的水平比例
    :param scale_y: y的变换比例，对应PS的垂直比例
    :return:
    """
    shape = bg.shape
    if len(shape) == 3:
        gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY).astype(float)
    else:
        gray = bg.astype(float)
    h,w = shape[:2]
    xs, ys = np.mgrid[0:w:1, 0:h:1]
    pos_x = scale_x * (gray - 128)/255 + xs
    pos_y = scale_y * (gray - 128)/255 + ys
    pos_x = np.clip(pos_x, 0, w-1).astype(int)
    pos_y = np.clip(pos_y, 0, h-1).astype(int)
    fg[ys,xs] = fg[pos_y, pos_x]
    return fg
