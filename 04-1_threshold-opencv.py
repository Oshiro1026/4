# threshold-opencv.py
import numpy as np
import cv2 as cv


th = 160  # 二値化の閾値

FN_INPUT = "sudoku.png"
# FN_OUTPUT = FN_INPUT + "_threshold{}.png".format(th)
FN_OUTPUT = f"{FN_INPUT}_threshold{th}.png"

image = cv.imread(FN_INPUT, cv.IMREAD_GRAYSCALE)

# 二値化をする
# 戻り値が2つあり、1つ目は与えた thresh と同じ値なので、
# 特に意味はないが、受け取る必要がある　→　変数を _ に置き換えることもある
_, image_b = cv.threshold(image, 
    thresh=th, maxval=255, type=cv.THRESH_BINARY)

cv.imwrite(FN_OUTPUT, image_b)


"""
Note:
    cv.threshold は画素値を 0 または maxval の2値に変換する（0 は固定）。
    画素値が閾値 (threshold value) 以下かそれ以外かで、
    どう処理されるかを type で決める。
    一部の type は、 0 や maxval に変換せずにそのまま画素値を残すものもある。
"""
