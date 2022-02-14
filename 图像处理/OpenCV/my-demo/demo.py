import cv2

img = cv2.imread('f:/images/reba.jpg')
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img', img)

w, h, ch = img.shape

for i in range(w):
    for j in range(h):
        for c in range(ch):
            img[i, j, c] = 255 - img[i, j, c]
            cv2.waitKey(1)
            cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()