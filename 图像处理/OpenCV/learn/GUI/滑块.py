
'''
创建滑块：createTrackbar
获取滑块值：getTracbarPos
'''

import cv2
import numpy as np
import bytools as byt

img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow('win', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('B', 'win', 0, 255, byt.do_nothing)

while True:
    b = cv2.getTrackbarPos('B', 'win')
    print(b)
    if cv2.waitKey(20) == 27:
        cv2.destroyAllWindows()
