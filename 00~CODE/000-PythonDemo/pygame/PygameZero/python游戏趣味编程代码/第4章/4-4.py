import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 800   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

balls = []  # 存储所有小球的信息，初始为空列表

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    for ball in balls:  # 绘制所有的圆
        screen.draw.filled_circle((ball[0], ball[1]), ball[4], (ball[5], ball[6], ball[7]))

def update():  # 更新模块，每帧重复操作
    for ball in balls:
        ball[0] = ball[0] + ball[2]   # 利用x方向速度更新x坐标
        ball[1] = ball[1] + ball[3]   # 利用y方向速度更新y坐标
        if ball[0] > WIDTH-ball[4] or ball[0] < ball[4]:  # 当小球碰到左右边界时，x方向速度反转
            ball[2] = -ball[2]
        if ball[1] > HEIGHT-ball[4] or ball[1] < ball[4]:  # 当小球碰到上下边界时，y方向速度反转
            ball[3] = -ball[3]

def on_mouse_move(pos, rel, buttons): # 当鼠标移动时
    if mouse.LEFT in buttons:         # 当鼠标左键按下时
        x = pos[0]   # 鼠标的x坐标，设为小球的x坐标
        y = pos[1]   # 鼠标的y坐标，设为小球的y坐标
        speed_x = random.randint(1, 5)  # 小球x方向的速度
        speed_y = random.randint(1, 5)  # 小球y方向的速度
        r = random.randint(5, 50)      # 小球的半径
        colorR = random.randint(10, 255)  # 小球的三个颜色分量
        colorG = random.randint(10, 255)
        colorB = random.randint(10, 255)
        # 存储小球所有信息的列表
        ball = [x, y, speed_x, speed_y, r, colorR, colorG, colorB]
        balls.append(ball)  # 把第该小球的信息添加到balls中

pgzrun.go()   # 开始执行游戏
