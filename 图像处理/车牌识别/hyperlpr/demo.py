#导入包
from hyperlpr import *
#导入OpenCV库
import cv2
#读入图片
image = cv2.imread("f:/images/chepai/b.jpg")
#识别结果
result = HyperLPR_plate_recognition(image)
print(result)

