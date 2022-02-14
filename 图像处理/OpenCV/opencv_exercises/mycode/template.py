import cv2
import numpy as np

def template_match(img, img_template, md):
    th, tw = img_template.shape[:2]
    result = cv2.matchTemplate(img, img_template, md)  # 得到匹配结果
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if md == cv2.TM_SQDIFF_NORMED:  # cv.TM_SQDIFF_NORMED最小时最相似，其他最大时最相似
        tl = min_loc
    else:
        tl = max_loc

    br = (tl[0] + tw, tl[1] + th)
    cv2.rectangle(img, tl, br, (0, 0, 255), 2)  # tl为左上角坐标，br为右下角坐标，从而画出矩形
    cv2.imshow("match-" + np.str(md), img)

# 三种模板匹配方法
# cv2.TM_SQDIFF_NORMED
# cv2.TM_CCORR_NORMED
# cv2.TM_CCOEFF_NORMED

# 读取模板
img_template = cv2.imread("f:/images/book_template.jpg")
# 读取图片
img = cv2.imread("f:/images/book2.jpg")

template_match(img, img_template, cv2.TM_CCORR_NORMED)



cv2.waitKey(0)
cv2.destroyAllWindows()