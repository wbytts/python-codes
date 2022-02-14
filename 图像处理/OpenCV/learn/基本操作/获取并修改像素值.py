import cv2

# 默认是以 BGR 格式读取进来的
img = cv2.imread("f:/images/a_zhu.jpg")

px = img[100, 100]
print(px)

# img[行, 列, 通道]
blue = img[100, 100, 0]
print(blue)

# 类似可以修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# 使用上面的方式可能会有点慢
# 使用 numpy的相关方法
print(img.item(100, 100, 2))
img.itemset((100, 100, 2), 100)
print(img.item(100, 100, 2))

cv2.imshow("azhu", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
