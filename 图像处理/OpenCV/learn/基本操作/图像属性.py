import cv2

src = cv2.imread('f:/images/a_zhu.jpg')

# 图像的shape
# 如果是灰度图，则返回仅有行数和列数
print('shape: ', src.shape) # shape，形状、宽高

# 返回图像像素个数
print('size', src.size)

# 返回图像的数据类型
print('dtype', src.dtype)

print('图片宽度:', src.shape[0])
print('图片高度:', src.shape[1])
if len(src.shape) >= 3:
    print('通道数目:', src.shape[2])
print('像素个数:', src.size)
print('像素数据类型:', src.dtype)

cv2.imshow('azhu', src)

cv2.waitKey(0)
cv2.destroyAllWindows()