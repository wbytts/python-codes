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
key = 1 # 定义按了哪个数字键，缺省为1
r = 3 # 定义了绘制小基本元素的大小，受鼠标左右移动控制

def update():  # 更新模块，每帧重复操作
    global key
    # 按下键盘数字键后，对key赋相应的值
    if keyboard.k_1:  
        key = 1
    elif keyboard.k_2:  
        key = 2
    elif keyboard.k_3:  
        key = 3
    elif keyboard.k_4:  
        key = 4
    elif keyboard.k_5:  
        key = 5
    elif keyboard.k_6:  
        key = 6
    elif keyboard.escape:  
        key = -1   

    XY.clear()  # 清空坐标列表
    RGB.clear()  # 清空颜色列表
    for i in range(100):
        x = random.randint(0, w-1)  # 取随机坐标
        y = random.randint(0, h-1)
        r, g, b = px[x, y]  # 取对应图片像素的颜色
        XY.append((x, y))   # 将位置信息添加到列表中
        RGB.append((r, g, b))  # 将颜色信息添加到列表中

def draw():  # 绘制模块，每帧重复执行
    if key == -1:  #当鼠标右键按下时
        screen.clear()  # 清除屏幕
    for i in range(100):
        x = XY[i][0] # 当前点坐标
        y = XY[i][1]
        box = Rect((x, y), (r, r))  # 画正方形区域的范围
        if key == 1:  # 绘制填充圆
            screen.draw.filled_circle(XY[i], r, RGB[i])
        if key == 2:  # 绘制空心圆
            screen.draw.circle(XY[i], r, RGB[i])
        if key == 3:  # 绘制线条
            screen.draw.line((x, y), (x+r, y+r), RGB[i])
        if key == 4:  # 绘制两条线条组成的叉号
            screen.draw.line((x-r, y-r), (x+r, y+r), RGB[i])
            screen.draw.line((x-r, y+r), (x+r, y-r), RGB[i])
        if key == 5:  # 绘制空心正方形
            screen.draw.rect(box, RGB[i])
        if key == 6:  # 绘制实心正方形
            screen.draw.filled_rect(box, RGB[i])

def on_mouse_move(pos, rel, buttons):  # 当鼠标移动时
    global r
    x = pos[0]   # 鼠标的x坐标
    r = x*10//WIDTH + 1  # 鼠标在最左边r=1，最右边r=10
    if mouse.RIGHT in buttons:   # 当鼠标右键按下时，准备清屏
        key == -1

pgzrun.go()  # 开始执行游戏
