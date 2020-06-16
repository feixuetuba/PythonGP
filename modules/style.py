"""
PS 风格
"""
import math

from cv2 import filter2D
import numpy as np

ANGLE0 = (1,0)
ANGLE45 = (0,0)
ANGLE90 = (0,1)
ANGLE135 = (0,2)
ANGLE180 = (1,2)
ANGLE225 = (2,2)
ANGLE270 = (2,1)
ANGLE315 = (2,0)

def emboss(image, angle=ANGLE45, height=1, offset=128, gray_mode=False):
    """
    八方浮雕
    :param image: 待处理图片
    :angle 旋转角度
    :return:
    """
    image = image.copy()
    kernel = np.array([[0,0,0], [0,1,0], [0,0,0]])
    kernel[angle] = -1
    shape = image.shape
    if gray_mode:
        c = 1
        image = image[..., None]
    else:
        assert shape[2] == 4, "image should be RGBA"
        c = 3
    image[...,:c] = filter2D(image[...,:c], c, kernel) * height
    image += offset
    image = np.clip(image, 0, 255)
    return image

def gray_emboss(image, angle:float, offset=128, gray_mode=False):
    image = image.copy()
    shape = image.shape
    angle = angle / 180 * math.pi
    step = math.pi / 4
    kernel = np.array([
        [math.cos(angle+step), math.cos(angle+2*step), math.cos(angle+3*step)],
        [math.cos(angle), 0, math.cos(angle+math.pi)],
        [math.cos(angle-step), math.cos(angle-2*step), math.cos(angle-3*step)]
    ])
    if gray_mode:
        c = 1
        image = image[..., None]
    else:
        assert shape[2] == 4, "image should be RGBA"
        c = 3
    image[...,:c] = filter2D(image[...,:c], c, kernel)
    image += offset
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