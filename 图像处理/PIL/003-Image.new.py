from PIL import Image

img1 = Image.open('f:/images/01.jpg')
img2 = Image.new('RGB', img1.size, 'red')
img3 = Image.blend(img1, img2, 0.5)
img3.show()
