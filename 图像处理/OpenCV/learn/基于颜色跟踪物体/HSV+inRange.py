import cv2
import numpy as np


# 从视频中提取指定颜色范围，并将其置为白，其余置为黑
def extract_object_demo():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()

        if ret is False:  # 如果没有获取到视频帧则返回false
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 43, 46])  # hsv中h，s，v的最小值
        upper_hsv = np.array([50, 255, 255])  # hsv中的h，s，v最大值

        # 提取指定范围颜色，保留指定范围颜色, 其余置为黑(0)
        mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  # 用inRange函数提取指定颜色范围，这里对hsv来处理
        cv2.imshow("video", frame)
        cv2.imshow("mask", mask)

        c = cv2.waitKey(40)
        if c == 27:
            break

extract_object_demo()