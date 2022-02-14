from PIL import Image

img = Image.open('f:/images/reba.jpg')  # 打开图片，返回一个Image实例
# img.show()  # 显示图片（使用系统工具显示）
print('图片格式:', img.format)
print('图片大小:', img.size)
print('图片的高度', img.height)
print('图片的宽度', img.width)
print('获取(100, 100)出的像素值', img.getpixel((100, 100)))
