'''
亮度：像素值的大小
对比度：像素值之间差值的大小（可求方差）
'''

import cv2
import numpy as np
import bytools

img = cv2.imread('f:/images/reba.jpg')
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)

cv2.imshow('img', img)

# 创建一个空白图像
empty = np.zeros(img.shape, img.dtype)
empty.fill(40)

dst = cv2.add(img, empty)
cv2.imshow('lightness change dst', dst)

contrast = np.zeros(img.shape, dtype=np.float32)
contrast.fill(2)
dst = cv2.multiply(np.float32(img), contrast)
cv2.imshow('contrast change dst', np.uint8(dst))

empty.fill(0)
dst = cv2.addWeighted(img, 1.5, empty, 0, 40)
cv2.imshow('addWeight', dst)

cv2.namedWindow('bars', cv2.WINDOW_GUI_NORMAL)
cv2.createTrackbar('bar', 'bars', 0, 200, bytools.do_nothing)
while True:
    cnt = cv2.getTrackbarPos('bar', 'bars') / 100
    print(cnt)
    dst = cv2.addWeighted(img, cnt, empty, 0, 40)
    cv2.imshow('addWeight', dst)
    if cv2.waitKey(20) == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()