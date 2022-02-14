import cv2
import sys
import bytools as byt


img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)



def mc(ev, x, y, flag, params):
    if ev == cv2.EVENT_LBUTTONDBLCLK:
        color = byt.random_color()
        cv2.circle(params, (x, y), 50, color, 2, cv2.LINE_8, 0)


cv2.setMouseCallback('img', mc, img)

while True:
    cv2.imshow("img", img)
    c = cv2.waitKey(20)
    if c == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
