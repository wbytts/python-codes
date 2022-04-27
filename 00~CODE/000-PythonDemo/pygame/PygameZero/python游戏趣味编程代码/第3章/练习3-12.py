import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 800   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度
R = 50        # 圆圈半径

def draw():    # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    for x in range(0, WIDTH+1, R):  # x坐标遍历
        for y in range(0, HEIGHT+1, R):  # y坐标遍历
            # 绘制一个空心圆，坐标(x,y)，半径R，颜色随机
            screen.draw.circle((x, y), R, (random.randint(
                0, 255), random.randint(0, 255), random.randint(0, 255)))

def on_mouse_down(): # 当按下鼠标键时
    draw()  # 调用绘制函数

pgzrun.go()  # 开始执行游戏