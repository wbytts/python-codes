import cv2
import numpy as np

img = cv2.imread('f:/images/liu_tou.png')
cv2.imshow("img", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("gray", gray)

retval, thre = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval1, thre1 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

cv2.imshow('re1', img)
cv2.imshow('re2', thre)
cv2.imshow('re3', thre1)
cv2.imshow('re4', gaus)

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化
dst = cv2.filter2D(img, -1, kernel=kernel)
cv2.imshow("custom_blur_demo", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
