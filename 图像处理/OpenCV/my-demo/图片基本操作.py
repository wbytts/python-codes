import cv2
import numpy as np

img = cv2.imread('../images/messi5.jpg')

# 可以通过行和列访问一个位置的像素值
# 对于深度图片，只会返回深度
px = img[100, 100]
print(px)

# accessing only blue pixel
blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

# Numpy是一个优化的库，能够快速计算数组。
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 访问图片属性
print(img.shape)
print(img.size)
print(img.dtype)
pixel_data = np.array(img)
print(pixel_data)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
