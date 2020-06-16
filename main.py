import cv2

from utils.common import show, imopen
from modules.distort import displacement
from modules.mixture import overlay
from modules import style

@show
def show_effect():
    import numpy as np
    checkerboard = imopen("resources/checkerboard.jpg")
    bg = imopen("resources/bg.png")
    em1 = style.emboss(bg, offset=128)
    em2 = style.emboss(bg, offset=128, height=2)
    em3 = style.emboss(bg, offset=128, height=3)
    em5 = style.emboss(bg, offset=128, height=5)
    ret = displacement(em5, checkerboard, 30, 30)
    ret = overlay(em5, ret)
    return np.hstack([em1, em2, em3, em5, ret, bg])

if __name__ == "__main__":
    show_effect()

