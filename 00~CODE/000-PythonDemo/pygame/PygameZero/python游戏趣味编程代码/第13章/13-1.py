import pgzrun  # 导入游戏库
from PIL import Image # 导入图像处理库

# 打开一个图像文件，注意是文件路径
im = Image.open('images\image1.jpg')
w, h = im.size  # 获得图像文件尺寸

WIDTH = w  # 设置窗口的宽度
HEIGHT = h  # 设置窗口的高度
pic = Actor('image1')  # 导入图片

def draw():  # 绘制模块，每帧重复执行
    pic.draw()  # 绘制图片

pgzrun.go()  # 开始执行游戏