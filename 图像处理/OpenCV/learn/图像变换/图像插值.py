'''
常见的插值算法：
    临界点插值：INTER_NEAREST
    双线性插值：INTER_LINEAR
    双立方插值：INTER_CUBIC
    ......
'''

import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)

dst = cv2.resize(img, (20, 20), interpolation=cv2.INTER_CUBIC)
cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()