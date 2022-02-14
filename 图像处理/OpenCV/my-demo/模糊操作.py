import cv2

image = cv2.imread("../images/lena.jpg")
result = cv2.blur(image, (15,15))
cv2.imshow("res", result)

cv2.waitKey(0)
cv2.destroyAllWindows()