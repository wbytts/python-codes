import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)

# 0 上下翻转
# 1 左右翻转
img = cv2.flip(img, 1)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
