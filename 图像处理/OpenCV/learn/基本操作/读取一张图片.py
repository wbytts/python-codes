import cv2

"""
imread：读取一张图片
    第一个参数：图片的路径
    第二个参数：图片的读取模式
        IMREAD_GRAYSCALE：加载灰度图像
        IMREAD_ANYCOLOR：读进来所有的通道

namedWindow：声明一个窗口
    第一个参数：窗口名称
    第二个参数：窗口类型

imshow：在指定窗口显示指定图片
    第一个参数：窗口名称
    第二个参数：图片对象（img读进来的）

waitkey：等待用户按键
    参数：等待的时间
    
destoryAllWindows：销毁所有窗口
"""
img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
