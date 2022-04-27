import pgzrun  # 导入游戏库
WIDTH = 800   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

class Ball: # 定义小球类
    x = WIDTH/2  # 小球的x坐标
    y = HEIGHT/2  # 小球的y坐标
    vx = 3  # 小球x方向的速度
    vy = 5  # 小球y方向的速度
    radius = 30  # 小球的半径
    color = 'red'  # 小球的颜色

ball = Ball() # 定义ball对象

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    # 绘制一个填充圆，坐标(x,y)，半径r，颜色
    screen.draw.filled_circle((ball.x, ball.y), ball.radius, ball.color)

def update():  # 更新模块，每帧重复操作
    ball.x += ball.vx   # 利用x方向速度更新x坐标
    ball.y += ball.vy   # 利用y方向速度更新y坐标
    # 当小球碰到左右边界时，x方向速度反转
    if ball.x > WIDTH-ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx
    # 当小球碰到上下边界时，y方向速度反转
    if ball.y > HEIGHT-ball.radius or ball.y < ball.radius:
        ball.vy = -ball.vy

pgzrun.go()   # 开始执行游戏
