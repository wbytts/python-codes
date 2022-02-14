import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画矩形
'''
def rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None): # real signature unknown; restored from __doc__
    """
    rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
    .   @brief Draws a simple, thick, or filled up-right rectangle.
    .   
    .   The function cv::rectangle draws a rectangle outline or a filled rectangle whose two opposite corners
    .   are pt1 and pt2.
    .   
    .   @param img Image.
    .   @param pt1 Vertex of the rectangle.
    .   @param pt2 Vertex of the rectangle opposite to pt1 .
    .   @param color Rectangle color or brightness (grayscale image).
    .   @param thickness Thickness of lines that make up the rectangle. Negative values, like #FILLED,
    .   mean that the function has to draw a filled rectangle.
    .   @param lineType Type of the line. See #LineTypes
    .   @param shift Number of fractional bits in the point coordinates.
    """
    pass
'''
cv2.rectangle(img, (200, 200), (300, 500), (0, 255, 0), 3)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
