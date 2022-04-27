from PIL import Image  # 导入图像处理库
import pgzrun  # 导入游戏库
import random  # 导入随机库

im = Image.open("images\\image2.jpg")  # 打开图像文件
w, h = im.size  # 获得图像文件尺寸
WIDTH = w  # 设置窗口的宽度
HEIGHT = h  # 设置窗口的高度
px = im.load()  # 导入图片像素

def update():  # 更新模块，每帧重复操作
    global r, g, b, x, y
    x = random.randint(0, w-1) # 取随机坐标
    y = random.randint(0, h-1) 
    r, g, b = px[x, y]  # 取对应图片像素的颜色

def draw():  # 绘制模块，每帧重复执行
    global r, g, b, x, y
    screen.draw.filled_circle((x, y), 5, (r, g, b)) #绘制一个填充圆
pgzrun.go()  # 开始执行游戏
