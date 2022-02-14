import cv2
import numpy as np

bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
camera = cv2.VideoCapture("f:/images/test.mp4")

while True:
    ret, frame = camera.read()
    fgmask = bs.apply(frame)
    fg2 = fgmask.copy()
    th = cv2.threshold(fg2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
    image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) > 100:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
    cv2.imshow("mog", fgmask)
    cv2.imshow("thresh", th)
    cv2.imshow("detection", frame)
    if cv2.waitKey(24) & 0xff == 27:
        break

camera.release()
cv2.destroyAllWindows()
