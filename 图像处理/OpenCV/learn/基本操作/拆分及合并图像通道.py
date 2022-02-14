import cv2
import numpy as np

img = cv2.imread("f:/images/a_zhu.jpg")

# 拆分
b, g, r = cv2.split(img)

# 合并
# img = cv2.merge(b, g, r)

# 或者使用如下方式
# b = img[:, :, 0]
# g = img[:, :, 1]
# r = img[:, :, 2]

print(img.shape)

b_channel = np.ones(img.shape, img.dtype)
g_channel = np.ones(img.shape, img.dtype)
r_channel = np.ones(img.shape, img.dtype)

b_channel[:, :, 0] = b_channel[:, :, 0] * b
g_channel[:, :, 1] = b_channel[:, :, 1] * g
r_channel[:, :, 2] = b_channel[:, :, 2] * r




cv2.imshow("azhu", img)
cv2.imshow('blue_channel', b_channel)
cv2.imshow('green_channel', g_channel)
cv2.imshow('red_channel', r_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
