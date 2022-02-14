import cv2

# 读取一张图片
src = cv2.imread("f:/images/lena.jpg")
# 命名一个窗口
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# 显示一张图片
cv2.ellipse(src,(256,256),(100,50),0,0,180,255,-1)
cv2.imshow("input image", src)
# 等待键盘按键
cv2.waitKey(0)
# 销毁所有窗口
cv2.destroyAllWindows()