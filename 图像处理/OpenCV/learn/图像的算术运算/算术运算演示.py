import cv2

# Linux
img1 = cv2.imread("f:/images/01.jpg")
# Windows
img2 = cv2.imread("f:/images/02.jpg")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

# 图像加法
# Numpy式加法
result = img1 + img2
cv2.imshow("img1 + img2", result)
# OpenCV加法
result = cv2.add(img1, img2)
cv2.imshow("cv2.add(img1, img2)", result)

# 图像混合
# g (x) = (1 − α) f0 (x) + αf1 (x)
# α 是权重
# dst = α · img1 + β · img2 + γ
img5 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow("cv2.addWeighted(img1, 0.7, img2, 0.3, 0)", img5)

# 位运算
# 按位与
result = cv2.bitwise_and(img1, img2)
cv2.imshow("cv2.bitwise_and(img1, img2)", result)
# 按位或
result = cv2.bitwise_or(img1, img2)
cv2.imshow("cv2.bitwise_or(img1, img2)", result)
# 按位异或
result = cv2.bitwise_xor(img1, img2)
cv2.imshow("cv2.bitwise_xor(img1, img2)", result)

# 按位取反
result = cv2.bitwise_not(img1)
cv2.imshow("cv2.bitwise_not(img1)", result)
result = cv2.bitwise_not(img2)
cv2.imshow("cv2.bitwise_not(img2)", result)


cv2.waitKey(0)
cv2.destroyAllWindows()