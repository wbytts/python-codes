import numpy as np
import cv2
cap = cv2.VideoCapture(0)

"""
我们这次创建一个VideoWriter对象。我们应该指定输出文件名（比如：output.avi），然后我们应该指定FourCC代码（下段详细介绍）。 
还有每秒帧数（fps）和帧的大小。最后是isColor标志。如果是True，编码器需要彩色帧。否则就是灰度帧。

FourCC是一个4为的代码，用来指定视频编码。可用的视频编码列表可以在fourcc.org找到。这个是跨平台的。下面这些编码都能用：

·In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID 更推荐. MJPG results in high size video. X264 gives very small size video)

In Windows: DIVX (More to be tested and added)

FourCC代码通过 cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')传入，或者cv2.VideoWriter_fourcc(*'MJPG')

"""

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()