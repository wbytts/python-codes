import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 1200   # 设置窗口的宽度
HEIGHT = 800  # 设置窗口的高度
balls = []  # 存储所有小球的信息，初始为空列表

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    for ball in balls:  # 绘制所有的圆
        screen.draw.filled_circle((ball[0], ball[1]), ball[2], (ball[3], ball[4], ball[5]))
        for x in range(1, ball[2], 3): # 用同心圆填充
            screen.draw.filled_circle((ball[0], ball[1]), ball[2]-x, (random.randint(
                ball[3], 255), random.randint(ball[4], 255), random.randint(ball[5], 255)))

def on_mouse_move(pos, rel, buttons): # 当鼠标移动时
    if mouse.LEFT in buttons:         # 当鼠标左键按下时
        x = pos[0]   # 鼠标的x坐标，设为小球的x坐标
        y = pos[1]   # 鼠标的y坐标，设为小球的y坐标
        r = random.randint(10, 20)      # 小球的半径
        colorR = random.randint(10, 255)  # 小球的三个颜色分量
        colorG = random.randint(10, 255)
        colorB = random.randint(10, 255)
        # 存储小球所有信息的列表
        ball = [x, y, r, colorR, colorG, colorB]
        balls.append(ball)  # 把第i号小球的信息添加到balls中

pgzrun.go()   # 开始执行游戏