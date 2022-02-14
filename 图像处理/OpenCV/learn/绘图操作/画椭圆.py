import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# 画椭圆
'''
def ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None): # real signature unknown; restored from __doc__
    """
    ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img
    .   @brief Draws a simple or thick elliptic arc or fills an ellipse sector.
    .   
    .   The function cv::ellipse with more parameters draws an ellipse outline, a filled ellipse, an elliptic
    .   arc, or a filled ellipse sector. The drawing code uses general parametric form.
    .   A piecewise-linear curve is used to approximate the elliptic arc
    .   boundary. If you need more control of the ellipse rendering, you can retrieve the curve using
    .   #ellipse2Poly and then render it with #polylines or fill it with #fillPoly. If you use the first
    .   variant of the function and want to draw the whole ellipse, not an arc, pass `startAngle=0` and
    .   `endAngle=360`. If `startAngle` is greater than `endAngle`, they are swapped. The figure below explains
    .   
    .   
    .   ![Parameters of Elliptic Arc](pics/ellipse.svg)
    .   
    .   @param img Image.
    .   @param center Center of the ellipse.
    .   @param axes Half of the size of the ellipse main axes.
    .   @param angle Ellipse rotation angle in degrees.
    .   @param startAngle Starting angle of the elliptic arc in degrees.
    .   @param endAngle Ending angle of the elliptic arc in degrees.
    .   @param color Ellipse color.
    .   @param thickness Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that
    .   a filled ellipse sector is to be drawn.
    .   @param lineType Type of the ellipse boundary. See #LineTypes
    .   @param shift Number of fractional bits in the coordinates of the center and values of axes.
    
    
    
    ellipse(img, box, color[, thickness[, lineType]]) -> img
    .   @overload
    .   @param img Image.
    .   @param box Alternative ellipse representation via RotatedRect. This means that the function draws
    .   an ellipse inscribed in the rotated rectangle.
    .   @param color Ellipse color.
    .   @param thickness Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that
    .   a filled ellipse sector is to be drawn.
    .   @param lineType Type of the ellipse boundary. See #LineTypes
    """
    pass
'''
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
