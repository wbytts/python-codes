import cv2

src = cv2.imread("f:/images/a_zhu.jpg")

cv2.imshow("azhu", src)

"""
imwrite：将一张图片写入到磁盘
    第一个参数：保存的路径
    第二个参数：要保存的图片对象

注意：不支持git格式的保存
"""
cv2.imwrite("f:/images/save.jpg", src)

cv2.waitKey(0)
cv2.destroyAllWindows()