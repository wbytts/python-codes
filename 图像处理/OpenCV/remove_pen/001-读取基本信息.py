import cv2

# 读取一张图片
src = cv2.imread("f:/images/OCR/wang_jing_shijuan-01.jpg")
# 命名一个窗口
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# 显示一张图片
cv2.imshow("input image", src)

# 等待键盘按键
cv2.waitKey(0)
# 销毁所有窗口
cv2.destroyAllWindows()
