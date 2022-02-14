import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画多边形
'''
def polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None): # real signature unknown; restored from __doc__
    """
    polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> img
    .   @brief Draws several polygonal curves.
    .   
    .   @param img Image.
    .   @param pts Array of polygonal curves.
    .   @param isClosed Flag indicating whether the drawn polylines are closed or not. If they are closed,
    .   the function draws a line from the last vertex of each curve to its first vertex.
    .   @param color Polyline color.
    .   @param thickness Thickness of the polyline edges.
    .   @param lineType Type of the line segments. See #LineTypes
    .   @param shift Number of fractional bits in the vertex coordinates.
    .   
    .   The function cv::polylines draws one or more polygonal curves.
    """
    pass
'''
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, pts, True, (255, 0, 0), 3)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
