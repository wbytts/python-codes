import cv2
import numpy as np


def video_demo():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)  # 将图片左右变换一下
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("video", frame)
        cv2.imshow("gray video", gray)
        c = cv2.waitKey(50)
        if c == 27:
            cv2.destroyAllWindows("video")
            cv2.destroyAllWindows("gray video")
            break


def get_image_info(image):
    print("="*20)
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def read_image(path):
    src = cv2.imread(path)
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    # cv.namedWindow("video", cv.WINDOW_AUTOSIZE)
    get_image_info(src)
    cv2.imshow("input image", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = "images/mask_Crystal.jpg"
# read_image(path)
video_demo()
