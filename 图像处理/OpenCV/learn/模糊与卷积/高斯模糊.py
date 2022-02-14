import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)

# 如果ksize设置了值（大于0），则sigmax不起作用
# 如果ksize都是0，则通过sigmax反算ksize进行执行
dst = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()