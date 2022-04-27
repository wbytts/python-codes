from PIL import Image  # 导入图像处理库
import pgzrun  # 导入游戏库
import random  # 导入随机库

im = Image.open("images\\image2.jpg")  # 打开图像文件
w, h = im.size  # 获得图像文件尺寸
WIDTH = w  # 设置窗口的宽度
HEIGHT = h  # 设置窗口的高度
px = im.load()  # 导入图片像素
XY = [] # 列表中存储点坐标
RGB = [] # 列表中存储对应的像素颜色值

def update():  # 更新模块，每帧重复操作
    XY.clear() # 清空列表
    RGB.clear()
    for i in range(100):
        x = random.randint(0, w-1)  # 取随机坐标
        y = random.randint(0, h-1)
        r, g, b = px[x, y]  # 取对应图片像素的颜色
        XY.append((x, y))   # 将位置信息添加到列表中
        RGB.append((r, g, b))  # 将颜色信息添加到列表中

def draw():  # 绘制模块，每帧重复执行
    for i in range(100):
        screen.draw.filled_circle(XY[i], 2, RGB[i])  # 绘制填充圆

pgzrun.go()  # 开始执行游戏