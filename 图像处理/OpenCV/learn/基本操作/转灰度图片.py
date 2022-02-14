import cv2

src = cv2.imread("f:/images/a_zhu.jpg")

# 色彩空间转换，BGR 到 GRAY
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


cv2.imshow("azhu", src)

cv2.waitKey(0)
cv2.destroyAllWindows()