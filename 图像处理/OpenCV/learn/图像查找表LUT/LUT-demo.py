import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()