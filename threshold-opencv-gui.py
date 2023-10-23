import numpy as np
import cv2 as cv

def trackbar_handler(x):
    pass

image = cv.imread("sudoku.png", cv.IMREAD_GRAYSCALE)
H, W = image.shape

scale = 320 / W

cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('threshold', 'image', 0, 255, trackbar_handler)

while cv.getWindowProperty('image', cv.WND_PROP_VISIBLE):
    image_scaled = cv.resize(image, dsize=(0, 0), fx=scale, fy=scale)

    th = cv.getTrackbarPos('threshold', 'image')
    _, image_scaled_thres = cv.threshold(image_scaled, th, maxval=255, type=cv.THRESH_BINARY)

    cv.imshow('image', np.concatenate((image_scaled, image_scaled_thres), axis=1))

    k = cv.waitKey(100) & 0xFF
    if k == 27:
        break




cv.destroyAllWindows()
