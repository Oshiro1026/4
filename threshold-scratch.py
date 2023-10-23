# threshold-scratch.py
# 2重ループで、一画素ずつ計算して書き込む実装
import numpy as np
import cv2 as cv


th = 127  # 二値化の閾値

FN_INPUT = "sudoku.png"
FN_OUTPUT = FN_INPUT + "_scratch{}.png".format(th)

image = cv.imread(FN_INPUT, cv.IMREAD_GRAYSCALE)
H, W = image.shape

image_b = np.zeros_like(image)  # 同じサイズの黒画像

for y in range(H):
    for x in range(W):
        # この下を自分で実装する
        pass  # これは消してよい

cv.imwrite(FN_OUTPUT, image_b)

"""
Note:
    cv.threshold(..., maxval=255, type=cv.THRESH_BINARY) 相当の
    結果になるようにすること。

Hint:
    あらかじめ 0 の配列を作っているので、
    255 (maxval) にすべき時だけ、配列に書き込めばよい。
"""
