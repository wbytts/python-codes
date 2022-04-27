import cv2
import pytesseract
import numpy as np


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(img, width=None, height=None):
    (rows, cols) = img.shape[:2]
    if width is None and height is None:
        return img
    elif width is None:
        ar = float(height) / rows
        width = int(ar * cols)
    else:
        ar = float(width) / cols
        height = int(ar * rows)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img


def repts(pts):
    print('1')
    rect = np.zeros((4, 2), dtype=np.float32)
    pt_sum = pts.sum(axis=1)
    pt_diff = np.diff(pts, axis=1)
    rect[0] = pts[np.argmin(pt_sum)]
    rect[2] = pts[np.argmax(pt_sum)]
    rect[1] = pts[np.argmin(pt_diff)]  # 高维度减去地维度
    rect[3] = pts[np.argmax(pt_diff)]
    return rect


# 图像预处理
image_org = cv2.imread('f:/images/OCR/wang_jing_shijuan-01.jpg')
image = resize(image_org, height=500)
cv_show('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv_show('gray', gray)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
cv_show('gray', gray)
canny = cv2.Canny(gray, 70, 150)
cv_show('canny', canny)
# 检测轮廓
cnts = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:3]
image_draw = image.copy()
image_draw = cv2.drawContours(image_draw, cnts, 0, (0, 0, 255), 2, 8)
cv_show("image_draw", image_draw)  # 提取出边缘轮廓
# 进行透视变换
pts = cv2.approxPolyDP(cnts[0], 0.02 * cv2.arcLength(cnts[0], closed=True), closed=True)
pts = np.reshape(pts, (4, 2)) * (image_org.shape[0] / 500)
pts = repts(pts)  # 重新排序 0-1-2-3 顺时针
new_height = int(max(np.sqrt(np.sum(np.square(pts[0] - pts[3]))), np.sqrt(np.sum(np.square(pts[1] - pts[2])))))
new_width = int(max(np.sqrt(np.sum(np.square(pts[0] - pts[1]))), np.sqrt(np.sum(np.square(pts[2] - pts[3])))))
new_pts = np.array([[0, 0], [new_width - 1, 0], [new_width - 1, new_height - 1], [0, new_height - 1]], dtype=np.float32)
M = cv2.getPerspectiveTransform(pts, new_pts)
img = cv2.warpPerspective(image_org, M, (new_width, new_height))
img_resize = resize(img, height=500)
cv_show('img_resize', img_resize)
# 识别文字,写文件
txt = pytesseract.image_to_string(img_resize)
with open('f:/images/OCR/wang_jing_shijuan-01.jpg.txt', 'w') as f:
    f.write(txt)
