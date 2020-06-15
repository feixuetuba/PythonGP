import cv2

from utils.common import show, imopen
from modules.distort import displacement
from modules.mixture import overlay
from modules.style import emboss

@show
def show_effect():
    checkerboard = imopen("resources/checkerboard.jpg")
    bg = imopen("resources/bg.png")
    ret = displacement(bg, checkerboard, 10, 10)
    ret = overlay(bg, ret)
    return  ret

if __name__ == "__main__":
    show_effect()

