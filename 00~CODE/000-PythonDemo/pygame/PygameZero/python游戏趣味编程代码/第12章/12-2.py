import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 600   # 设置窗口的宽度
HEIGHT = 800  # 设置窗口的高度
time = 0  # 游戏坚持的时间

class Ball: # 定义小球类
    x = None  # 小球的x坐标
    y = None  # 小球的y坐标
    vx = None  # 小球x方向的速度
    vy = None  # 小球y方向的速度
    radius = None  # 小球的半径
    color = None  # 小球的颜色

    # 使用构造函数传递参数对对象初始化
    def __init__(self,x,y,vx,vy,radius,color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
    
    def draw(self): # 绘制函数
        # 绘制一个填充圆，坐标(x,y)，半径radius，颜色color
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self): # 更新小球的位置、速度
        self.x += self.vx   # 利用x方向速度更新x坐标
        self.y += self.vy   # 利用y方向速度更新y坐标
        # 当小球碰到左右边界时，x方向速度反转
        if self.x > WIDTH-self.radius or self.x < self.radius:
            self.vx = -self.vx
        # 当小球碰到上下边界时，y方向速度反转
        if self.y > HEIGHT-self.radius or self.y < self.radius:
            self.vy = -self.vy

balls = []  # 存储所有小球的信息，初始为空列表

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    for ball in balls:
        ball.draw()   # 绘制小球

def update():  # 更新模块，每帧重复操作
    for ball in balls:
        ball.update()  # 更新小球的位置、速度

def count(): # 此函数每秒运行一次
    global time
    time += 1 # 计时，每秒钟时间+1
    # 每隔1秒，加一个小球，并且小球数目不超过20
    if time % 1 == 0 and len(balls) <= 20:
        x = WIDTH//2   # 设为小球的x坐标
        y = random.randint(5, HEIGHT//10)   # 设为小球的y坐标
        vx = random.choice([-3, -2, -1, 1, 2, 3])  # 小球x方向的速度
        vy = random.randint(1, 3)  # 小球y方向的速度
        r = 3      # 小球的半径
        color = 'black'  # 小球的颜色
        ball = Ball(x, y, vx, vy, r, color)  # 定义ball对象
        balls.append(ball)  # 把该小球的信息添加到balls中
    clock.schedule_unique(count, 1)  # 下一次隔1秒调用count()函数

count()  # 调用函数运行
pgzrun.go()   # 开始执行游戏
