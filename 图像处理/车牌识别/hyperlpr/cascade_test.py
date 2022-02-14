import cv2

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    chepai_cascade = cv2.CascadeClassifier('./cascade.xml')
    cards = chepai_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if (len(cards) == 0):
        return None, None

    (x, y, w, h) = cards[0]

    return gray[y:y + w, x:x + h], cards[0]


image = cv2.imread("f:/images/chepai/b.jpg")
result = detect_face(image)
print(result)
pos = result[1]
cv2.rectangle(image, (pos[0], pos[1]), (pos[0]+pos[2], pos[1]+pos[3]), (0, 0, 255), 2, 8, 0)
cv2.imshow("result", image)
cv2.waitKey()
cv2.destroyAllWindows()

