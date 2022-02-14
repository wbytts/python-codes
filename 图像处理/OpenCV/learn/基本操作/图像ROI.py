import cv2

img = cv2.imread("f:/images/a_zhu.jpg")

# img[ x_start:x_end, y_start:y_end ]
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow("azhu", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
