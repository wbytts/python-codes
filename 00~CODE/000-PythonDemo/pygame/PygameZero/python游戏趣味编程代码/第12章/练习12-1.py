import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 800   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

# 候选的7种颜色之一
Colors = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple']

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
    
    def draw(self):
        # 绘制一个填充圆，坐标(x,y)，半径radius，颜色color
        screen.draw.circle((self.x, self.y), self.radius, self.color)

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

def on_mouse_move(pos, rel, buttons):  # 当鼠标移动时
    if mouse.LEFT in buttons:         # 当鼠标左键按下时
        x = pos[0]   # 鼠标的x坐标，设为小球的x坐标
        y = pos[1]   # 鼠标的y坐标，设为小球的y坐标
        vx = random.randint(1, 5)  # 小球x方向的速度
        vy = random.randint(1, 5)  # 小球y方向的速度
        r = random.randint(5, 20)      # 小球的半径
        color = Colors[random.randint(0, 6)]  # 小球的颜色
        ball = Ball(x, y, vx, vy, r, color)  # 定义ball对象
        balls.append(ball)  # 把第该小球的信息添加到balls中

pgzrun.go()   # 开始执行游戏
