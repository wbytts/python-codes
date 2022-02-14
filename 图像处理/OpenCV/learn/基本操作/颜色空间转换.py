import cv2

# 默认读进来是 BGR
img = cv2.imread("f:/images/a_zhu.jpg")
cv2.imshow("azhu", img)

# 转换成灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", img_gray)

'''
在 OpenCV 的 HSV 格式中， H（色彩/色度）的取值范围是 [0， 179]，
S（饱和度）的取值范围 [0， 255]， V（亮度）的取值范围 [0， 255]。但是不
同的软件使用的值可能不同。所以当你需要拿 OpenCV 的 HSV 值与其他软
件的 HSV 值进行对比时，一定要记得归一化。
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
