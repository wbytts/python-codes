import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画圆
'''
def circle(img, center, radius, color, thickness=None, lineType=None, shift=None): # real signature unknown; restored from __doc__
    """
    circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
    .   @brief Draws a circle.
    .   
    .   The function cv::circle draws a simple or filled circle with a given center and radius.
    .   @param img Image where the circle is drawn.
    .   @param center Center of the circle.
    .   @param radius Radius of the circle.
    .   @param color Circle color.
    .   @param thickness Thickness of the circle outline, if positive. Negative values, like #FILLED,
    .   mean that a filled circle is to be drawn.
    .   @param lineType Type of the circle boundary. See #LineTypes
    .   @param shift Number of fractional bits in the coordinates of the center and in the radius value.
    """
    pass
'''
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
