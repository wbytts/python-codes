import numpy as np
import cv2


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv  # 修改
    cv2.imshow("pixels_demo", image)


def inverse(image):
    dst = cv2.bitwise_not(image)
    cv2.imshow("inverse learn", dst)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    # img = np.zeros([400, 400, 1], np.uint8)  # 单通道图片
    # img[:, :, 0] = np.ones([400, 400])*127   # 单通道设置灰度图
    img[:, :, 0] = np.ones([400, 400]) * 255
    # img[:, :, 1] = np.ones([400, 400])*255
    # img[:, :, 2] = np.ones([400, 400])*255
    cv2.imshow("new image", img)
    # cv2.imwrite("images/learn.img")


print("---------- Hello OpenCV ----------")
# src = cv2.imread("images/mask_Crystal.jpg")
# cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input image", src)
t1 = cv2.getTickCount()
# access_pixels(src)
create_image()
# inverse(src)

t2 = cv2.getTickCount()
time = (t2 - t1) / cv2.getTickFrequency()
print("time : %s ms" % (time * 1000))
cv2.waitKey(0)
cv2.destroyAllWindows()
