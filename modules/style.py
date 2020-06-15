"""
PS 风格
"""
from cv2 import filter2D
import numpy as np

def emboss(image, gray_mode=False):
    """
    浮雕
    :param image: 待处理图片
    :return:
    """
    image = image
    kernel = np.array([[1,0,0],[0,0,0],[0,0,-1]])
    shape = image.shape
    if gray_mode:
        c = 1
        image = image[..., None]
    else:
        assert shape[2] == 4, "image should be RGBA"
        c = 3
    image[...,:c] = filter2D(image[...,:c], c, kernel)
    image += 127
    image = np.clip(image, 0, 255)
    return image

def curved(image, gray_mode=False):
    """
    雕刻
    :param image: 待处理图片
    :return:
    """
    image = image.astype(float)
    kernel = np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 1]])
    shape = image.shape
    if gray_mode:
        c = 1
        image = image[..., None]
    else:
        assert shape[2] == 4, "image should be RGBA"
        c = 3
    image[..., :c] = filter2D(image[..., :c], c, kernel)
    image += 127
    image = np.clip(image, 0, 255)
    return image