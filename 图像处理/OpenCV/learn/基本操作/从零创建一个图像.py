import cv2 as cv
import numpy as np

# 第一种创建方法，从原图像拷贝
img = cv.imread("f:/images/reba.jpg")
dst = np.copy(img)
dst.fill(127)
cv.imshow('dst', dst)

# 第二种创建方法，直接使用numpy创建
blank = np.zeros([400, 400], dtype=np.uint8)
blank.fill(255)
cv.imshow('blank', blank)

# 第三种方式
t3 = np.zeros([40000], dtype=np.uint8)
t4 = np.reshape(t3, [200, 200])
cv.imshow('t3', t4)

# 第四种方式
clone = np.zeros(img.shape, img.dtype)
cv.imshow('colne', clone)

# 带有随机噪声
t5 = np.random.random_sample([400, 400]) * 255
# t5 = np.random.random_sample([400, 400, 3]) * 255 # 彩色噪声
# 也可以指定产生的颜色范围
t6 = np.uint8(t5)
cv.imshow('t6', t6)

cv.waitKey(0)
cv.destoryAllWindows()


