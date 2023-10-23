# threshold-opencv-adaptive.py
import numpy as np
import cv2 as cv


FN_INPUT = "sudoku.png"
FN_OUTPUT = FN_INPUT + "_adaptive.png"

image = cv.imread(FN_INPUT, cv.IMREAD_GRAYSCALE)

# 適応的な二値化をする
image_b = cv.adaptiveThreshold(
    image, maxValue=255, 
    thresholdType=cv.THRESH_BINARY, 
    adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    blockSize=9, C=2
    # blockSize=13, C=5
)

cv.imwrite(FN_OUTPUT, image_b)


"""
Note:
    cv.adaptiveThreshold は各画素毎に閾値を決めて二値化する。
    閾値は各画素を中心とした blockSize 四方の領域の平均から
    指定した定数Cを引いたものを使う。
    これは、陰影など明るさが一定していない場合に有用であるが、
    blockSize, C を適切に決める方法はない。
    blockSize は必ず奇数でなければならない。

    cv.threshold と引数の順序やキーワード、戻り値が全く異なるので注意。
"""