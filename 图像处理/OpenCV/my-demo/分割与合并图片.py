import cv2
import numpy as np

img = cv2.imread('../images/messi5.jpg')

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# 或者 b = img[:,:,0]

# 把所有的红色像素变为0 img[:,:,2]=0

# 注：cv2.split()是一个成本很高的操作（执行时间），所以只在必要的时候使用。Numpy索引要更有效率，能用就用。

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
