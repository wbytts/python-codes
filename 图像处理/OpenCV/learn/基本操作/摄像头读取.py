import cv2

cap = cv2.VideoCapture(0) # 'http://admin:admin@192.168.1.3:8081/video'


def laplace_demo(image):  # 二阶导数，边缘更细
    dst = cv2.Laplacian(image,cv2.CV_32F)
    lpls = cv2.convertScaleAbs(dst)
    cv2.imshow("laplace_demo", lpls)

def sobel_demo(image):
    grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # 采用Scharr边缘更突出
    grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)

    gradx = cv2.convertScaleAbs(grad_x)  # 由于算完的图像有正有负，所以对其取绝对值
    grady = cv2.convertScaleAbs(grad_y)

    # 计算两个图像的权值和，dst = src1*alpha + src2*beta + gamma
    gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)

    cv2.imshow("gradx", gradx)
    cv2.imshow("grady", grady)
    cv2.imshow("gradient", gradxy)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #laplace_demo(frame)
    sobel_demo(frame)
    cv2.imshow('camera', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cv2.destroyAllWindows()
