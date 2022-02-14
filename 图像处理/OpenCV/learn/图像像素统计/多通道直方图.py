import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("f:/images/reba.jpg")
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.imshow("img", img)

h, w = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
hist = np.zeros([256], dtype=np.int32)
for row in range(h):
    for col in range(w):
        pv = gray[row, col]
        hist[pv] += 1

plt.plot(hist, color='r')
plt.xlim(0, 256)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
