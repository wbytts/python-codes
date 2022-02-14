import cv2

img = cv2.imread("f:/images/a_zhu.jpg")

cv2.imshow("azhu", img)

result = cv2.blur(img, (15, 15))
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
