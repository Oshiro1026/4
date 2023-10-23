# threshold-opencv-otsu.py
import numpy as np
import cv2 as cv


FN_INPUT = "sudoku.png"

image = cv.imread(FN_INPUT, cv.IMREAD_GRAYSCALE)

# 二値化をする
# cv.THRESH_OTSU を指定するときは閾値は無視されるので、
# ここでは 0 としている
# 1つ目の戻り値に Otsu の方法で定まる閾値が入っている
th, image_b = cv.threshold(image, 
    thresh=0, maxval=255, 
    type=cv.THRESH_BINARY | cv.THRESH_OTSU)

FN_OUTPUT = FN_INPUT + "_otsu-threshold{}.png".format(th)
cv.imwrite(FN_OUTPUT, image_b)


"""
Note:
    cv.threshold の type に cv.THRESH_OTSU を + または | で付加すると、
    閾値を大津の方法で計算する。
    この場合、 thresh は無視され、決定された閾値が1つ目の戻り値として返る。


1
2
3
4
5

8
16

5 -   00000101
8     00001000
5|8   00001101     
5+8+8 00010101

16   00010000
     



"""