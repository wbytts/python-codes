"""
首先我们创建一个鼠标回调函数，当一个鼠标事件发生时来执行。
鼠标事件可以是任何和鼠标左键点下，左键抬起，左键双击等相关的时间。
它会给我们每次鼠标事件的坐标（x,y）。
通过这些事件和坐标，我们可以做任何我们想做得，要列出所有可用的事件，执行下面的代码：
"""
import cv2

# 所有鼠标可用事件
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# 创建一个鼠标回调函数有通用的格式。区别只是这个函数是做什么的。
# 所以我们的鼠标回调函数只做一件事，双击的时候画一个圆。

import numpy as np


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 1024, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
