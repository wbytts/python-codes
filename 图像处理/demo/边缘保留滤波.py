#边缘保留滤波（EPF）  高斯双边、均值迁移
import cv2 as cv
import numpy as np

def bi_demo(image):   #双边滤波
    dst = cv.bilateralFilter(image, 0, 5, 5)
    cv.imwrite("a.png", dst)
    cv.namedWindow("bi_demo", cv.WINDOW_NORMAL)
    cv.imshow("bi_demo", dst)

def shift_demo(image):   #均值迁移
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.namedWindow("shift_demo", cv.WINDOW_NORMAL)
    cv.imshow("shift_demo", dst)

src = cv.imread('f:/images/liu_tou.png')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)

bi_demo(src)
shift_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()