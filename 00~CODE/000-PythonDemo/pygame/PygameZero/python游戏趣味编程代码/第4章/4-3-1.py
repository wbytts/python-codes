import pgzrun  # 导入游戏库
WIDTH = 800   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度
x = WIDTH/2   # 小球的x坐标，初始化再窗口中间
y = HEIGHT/2  # 小球的y坐标，初始化再窗口中间
speed_x = 3   # 小球x方向的速度
speed_y = 5   # 小球y方向的速度
r = 30        # 小球的半径
colorR = 255  # 小球的三个颜色分量
colorG = 0
colorB = 0

# 存储小球所有信息的列表
ball = [x, y, speed_x, speed_y, r, colorR, colorG, colorB]

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    # 绘制一个填充圆，坐标(x,y)，半径r，颜色
    screen.draw.filled_circle(
        (ball[0], ball[1]), ball[4], (ball[5], ball[6], ball[7]))

def update():  # 更新模块，每帧重复操作
    ball[0] = ball[0] + ball[2]   # 利用x方向速度更新x坐标
    ball[1] = ball[1] + ball[3]   # 利用y方向速度更新y坐标
    if ball[0] > WIDTH-ball[4] or ball[0] < ball[4]:  # 当小球碰到左右边界时，x方向速度反转
        ball[2] = -ball[2]
    if ball[1] > HEIGHT-ball[4] or ball[1] < ball[4]:  # 当小球碰到上下边界时，y方向速度反转
        ball[3] = -ball[3]

pgzrun.go()   # 开始执行游戏