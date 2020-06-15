"""
PS 混合
"""
import numpy as np

def overlay(bg, fg, alpha=1.0):
    """
    alpha 透明度叠加，图片需要RGBA的.
    :param bg: 背景
    :param fg: 前景
    :param alpha:
    :return:
    """
    assert len(fg.shape) == 3, f"fg should be RGBA mode"
    assert len(bg.shape) == 3, f"bg should be RGBA mode"
    fg_h, fg_w, fg_c = fg.shape
    bg_h, bg_w, bg_c = bg.shape
    assert fg_h == bg_h, f"fg.h != bg.h"
    assert fg_w == bg_w, f"fg.w != bg.w"
    assert fg_c == bg_c == 4, f"fg.chanel != bg.chanel"
    fg = fg.astype(float)
    bg = bg.astype(float)
    weight_fg = alpha * fg[...,3:4]/255.0
    weight_bg = 1 - weight_fg
    result = bg * weight_bg + fg * weight_fg
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8, copy=False)


def screen(bg, fg):
    pass