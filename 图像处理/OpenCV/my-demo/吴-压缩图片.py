import cv2
import numpy as np

img = cv2.imread('f:/images/wu/010002_1.png')
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow('gray', gray)

print(img.shape)

res = np.zeros((100, img.shape[1], 3))


cv2.waitKey(0)
cv2.destroyAllWindows()
