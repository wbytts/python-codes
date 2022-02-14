import cv2

img = cv2.imread("f:/images/reba.jpg")
cv2.imshow("azhu", img)

# 灰度转换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 读取模型文件
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

# 探测图片中的人脸
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
    cv2.rectangle(img, (x, y), (x + w, y + w), (0, 255, 0), 2)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
