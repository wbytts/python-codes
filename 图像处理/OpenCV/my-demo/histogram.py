import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # image.ravel()将图像展开，256为bins数量，[0, 256]为范围
    plt.show()

def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):

        # 计算出直方图，calcHist(images, channels, mask, histSize(有多少个bin), ranges[, hist[, accumulate]]) -> hist
        # hist 是一个 256x1 的数组，每一个值代表了与该灰度值对应的像素点数目。

        hist = cv2.calcHist(image, [i], None, [256], [0, 256])
        print(hist.shape)
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

img = cv2.imread("f:/images/lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image_hist(img)

dst = cv2.equalizeHist(img)

cv2.imshow("res", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
