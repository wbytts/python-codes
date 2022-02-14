import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)

dst = cv2.blur(img, (30, 30))
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()