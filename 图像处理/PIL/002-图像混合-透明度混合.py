from PIL import Image

img1 = Image.open('f:/images/01.jpg')
img2 = Image.open('f:/images/02.jpg')

img3 = Image.blend(img1, img2, 0.5)
img3.show()
