"""
OpenCV加载的彩色图片是BGR模式的。但是Matplotlib显示的是RGB模式的。
所以彩色图片如果是通过OpenCV读入的在Matplotlib里会显示不正确。
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../images/01.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()



