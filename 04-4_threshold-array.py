# threshold-array.py
# OpenCV を使わずに、配列の条件指定で処理する
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


th = 50  # 二値化の閾値

FN_INPUT = "sudoku.png"
FN_OUTPUT = FN_INPUT + "_array{}.png".format(th)

image = cv.imread(FN_INPUT, cv.IMREAD_GRAYSCALE)

# 二値化をする
image_b = np.zeros_like(image)  # 入力画像と同じサイズの黒画像
plt.imshow(image > th)
plt.show()
image_b[image > th] = 255
# image_b[image <= th] = 0  # これは特にやらなくてよい

cv.imwrite(FN_OUTPUT, image_b)

"""
Note:
    numpy 配列のインデックスとして条件式を書くと、
    その条件を満たしている要素だけアクセスすることができる。
    それを利用すると、二値化が実現できる。

    np.zeros_like は、np.zeros と同じで全要素が 0 の配列を作るが、
    与えた配列と同じ shape, dtype にしてくれる便利関数である。
    np.zeros(image.shape, dtype=image.dtype) と同じ。  
"""
