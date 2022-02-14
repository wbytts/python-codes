import cv2

img = cv2.imread("f:/images/reba.jpg")

# 返回从参考点到这个函数执行时的时钟数
cv2.getTickCount()
# cv2.getCPUTickCount()

# 返回时钟频率，或者说每秒的时钟数
cv2.getTickFrequency()


# 所以可以使用以下方式计时
t1 = cv2.getTickCount()
# 做一些操作 。。。。。。
t2 = cv2.getTickCount()
# 计算时间（秒）
t = (t2 - t1) / cv2.getTickFrequency()

cv2.imshow("reba", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
