import cv2


def color_space_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    cv2.imshow("gray", gray)


src = cv2.imread("../images/lena.jpg")
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)

color_space_demo(src)

cv2.waitKey(0)
cv2.destroyAllWindows()
