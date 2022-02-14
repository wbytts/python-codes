import cv2
import numpy as np

'''
x = L * cos(u + a)
y = L * sin(u + a)

cos(u + a) = cos(u)*cos(a) - sin(u)*sin(a)
sin(u + a) = sin(u)*cos(a) + cos(u)*sin(a)

xx = L*cos(u)
yy = L*sin(u)
x = xx*cos(a) - yy*sin(a)
y = xx*sin(a) + yy*cos(a)
'''

img = cv2.imread('f:/images/reba.jpg')
cv2.imshow('img', img)
h, w, ch = img.shape
cx = w // 2
cy = h // 2
M = cv2.getRotationMatrix2D((cx, cy), 35, 1.0)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
sw = np.int(h * sin + w * cos)
sh = np.int(h * cos + w * sin)
M[0, 2] += (sw/2) - cx
M[1, 2] += (sh/2) - cy
dst = cv2.warpAffine(img, M, (sw, sh))
cv2.imshow('dst', dst)

for i in range(0, 180000):
    M = cv2.getRotationMatrix2D((cx, cy), i, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    sw = np.int(h * sin + w * cos)
    sh = np.int(h * cos + w * sin)
    M[0, 2] += (sw / 2) - cx
    M[1, 2] += (sh / 2) - cy
    dst = cv2.warpAffine(img, M, (sw, sh))
    cv2.waitKey(10)
    cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()

