import cv2

cap = cv2.VideoCapture(0) # 'http://admin:admin@192.168.1.3:8081/video'
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print("发现{0}个人脸!".format(len(faces)))
    # 绘制矩形框住人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)
    cv2.imshow("result", frame)

    cv2.waitKey(200)

cv2.destroyAllWindows()
