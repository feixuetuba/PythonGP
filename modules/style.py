import cv2
from scipy.signal import convolve2d
import numpy as np

def emboss_effect(image):
    """
    浮雕
    :param image: 待处理图片
    :return:
    """
    image = image.astype(float)
    kernel = np.array([[1,0,0],[0,0,0],[0,0,-1]])
    h,w,c = image.shape
    for _ in range(c):
        image[...,_] = convolve2d(image[...,_], kernel, boundary='symm',mode='same')
    image += 127
    image = np.clip(image, 0, 255)
    return image.astype(np.uint8)

def curved_effect(image):
    """
    雕刻
    :param image: 待处理图片
    :return:
    """
    image = image.astype(float)
    kernel = np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 1]])
    h, w, c = image.shape
    for _ in range(c):
        image[..., _] = convolve2d(image[..., _], kernel, boundary='symm', mode='same')
    image += 127
    image = np.clip(image, 0, 255)
    return image.astype(np.uint8)