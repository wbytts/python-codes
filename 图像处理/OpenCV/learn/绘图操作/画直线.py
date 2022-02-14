import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画一条线
'''
def line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None): # real signature unknown; restored from __doc__
    """
    line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
    .   @brief Draws a line segment connecting two points.
    .   
    .   The function line draws the line segment between pt1 and pt2 points in the image. The line is
    .   clipped by the image boundaries. For non-antialiased lines with integer coordinates, the 8-connected
    .   or 4-connected Bresenham algorithm is used. Thick lines are drawn with rounding endings. Antialiased
    .   lines are drawn using Gaussian filtering.
    .   
    .   @param img Image.
    .   @param pt1 First point of the line segment.
    .   @param pt2 Second point of the line segment.
    .   @param color Line color.
    .   @param thickness Line thickness.
    .   @param lineType Type of the line. See #LineTypes.
    .   @param shift Number of fractional bits in the point coordinates.
    """
    pass
参数说明：
    1. 要在哪个图上绘制
    2. 绘制的起点坐标
    3. 绘制的终点坐标
    4. 线条的颜色
    5. 线条的粗细
    6. 线条的样式
'''
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
