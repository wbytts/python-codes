import cv2

# user: admin
# pwd: 12345
# main: 主码流
# ip: 192.168.1.64
# Channels: 实时数据
# 1： 通道
cap = cv2.VideoCapture("rtsp://admin:123456@192.168.0.102:8554/live")
print(cap.isOpened())
while cap.isOpened():
    success, frame = cap.read()
    frame = cv2.bitwise_not(frame)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
