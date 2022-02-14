import cv2
import numpy as np

# 读取一张图片
src = cv2.imread("../images/CrystalLiu2.jpg")
# 命名一个窗口
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)

def fill_color_demo(image, x, y):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv2.floodFill(copyImg, mask, (x, y), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow("fill", copyImg)
    cv2.setMouseCallback('fill', draw_circle)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        fill_color_demo(src, x, y)



# 显示一张图片
cv2.imshow("input image", src)
cv2.setMouseCallback('input image', draw_circle)

# 等待键盘按键
cv2.waitKey(0)
# 销毁所有窗口
cv2.destroyAllWindows()