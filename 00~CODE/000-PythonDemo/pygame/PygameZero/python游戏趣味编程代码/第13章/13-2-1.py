import pgzrun  # 导入游戏库
from PIL import Image # 导入图像处理库

# 打开一个图像文件，注意是文件路径
im = Image.open('images\image1.jpg')

box = (200, 0, 950, 750)  # 设定剪裁区域在原图中的左上角、右下角坐标
region = im.crop(box) # 利用box对图像im进行剪裁
w, h = region.size  # 获得剪裁后的图像尺寸
region.save("images\image1_crop.jpg") #保存剪裁图像

WIDTH = w  # 设置窗口的宽度
HEIGHT = h  # 设置窗口的高度
pic = Actor('image1_crop')  # 导入图片

def draw():  # 绘制模块，每帧重复执行
    pic.draw()  # 绘制图片

pgzrun.go()  # 开始执行游戏
