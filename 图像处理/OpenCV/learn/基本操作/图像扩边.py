import cv2



'''
def copyMakeBorder(src, top, bottom, left, right, borderType, dst=None, value=None): # real signature unknown; restored from __doc__
    """
    copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) -> dst
    .   @brief Forms a border around an image.
    .   
    .   The function copies the source image into the middle of the destination image. The areas to the
    .   left, to the right, above and below the copied source image will be filled with extrapolated
    .   pixels. This is not what filtering functions based on it do (they extrapolate pixels on-fly), but
    .   what other more complex functions, including your own, may do to simplify image boundary handling.
    .   
    .   The function supports the mode when src is already in the middle of dst . In this case, the
    .   function does not copy src itself but simply constructs the border, for example:
    .   
    .   @code{.cpp}
    .   // let border be the same in all directions
    .   int border=2;
    .   // constructs a larger image to fit both the image and the border
    .   Mat gray_buf(rgb.rows + border*2, rgb.cols + border*2, rgb.depth());
    .   // select the middle part of it w/o copying data
    .   Mat gray(gray_canvas, Rect(border, border, rgb.cols, rgb.rows));
    .   // convert image from RGB to grayscale
    .   cvtColor(rgb, gray, COLOR_RGB2GRAY);
    .   // form a border in-place
    .   copyMakeBorder(gray, gray_buf, border, border,
    .   border, border, BORDER_REPLICATE);
    .   // now do some custom filtering ...
    .   ...
    .   @endcode
    .   @note When the source image is a part (ROI) of a bigger image, the function will try to use the
    .   pixels outside of the ROI to form a border. To disable this feature and always do extrapolation, as
    .   if src was not a ROI, use borderType | #BORDER_ISOLATED.
    .   
    .   @param src Source image.
    .   @param dst Destination image of the same type as src and the size Size(src.cols+left+right,
    .   src.rows+top+bottom) .
    .   @param top
    .   @param bottom
    .   @param left
    .   @param right Parameter specifying how many pixels in each direction from the source image rectangle
    .   to extrapolate. For example, top=1, bottom=1, left=1, right=1 mean that 1 pixel-wide border needs
    .   to be built.
    .   @param borderType Border type. See borderInterpolate for details.
    .   @param value Border value if borderType==BORDER_CONSTANT .  边界颜色 如果边界的类型是 cv2.BORDER_CONSTANT
    .   
    .   @sa  borderInterpolate
    """
    pass

borderType
    cv2.BORDER_CONSTANT
        添加有颜色的常数值边界，还需要下一个参数（ value）
        
    cv2.BORDER_REFLECT
        边界元素的镜像,比如fedcba|abcdefgh|hgfedcb
    
    cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
        gfedcb|abcdefgh|gfedcba
        
    cv2.BORDER_REPLICATE
        重复最后一个元素
        aaaaaa|abcdefgh|hhhhhhh
    
    cv2.BORDER_WRAP
        cdefgh|abcdefgh|abcdefg
'''

img = cv2.imread("f:/images/a_zhu.jpg")
cv2.copyMakeBorder(img, cv2.BORDER_REPLICATE)

cv2.imshow("azhu", img)

cv2.waitKey(0)
cv2.destroyAllWindows()