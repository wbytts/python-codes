import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 600   # 设置窗口的宽度
HEIGHT = 800  # 设置窗口的高度

time = 0  # 游戏坚持的时间
hero = Actor('hero')  # 导入玩家飞机图片
live = 3 # 飞机一共3条命

livePics = []  # 在左上角显示生命符号
for i in range(live):
    livePic = Actor('hero_small')
    livePic.x = 40 + i*60
    livePic.y = 40
    livePics.append(livePic)

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

class SmartBall(Ball): # 定义聪明小球类，继承Ball而来
    targetX = None
    targetY = None
    # 使用构造函数传递参数对对象初始化
    def __init__(self, x, y, vx, vy, radius, color,targetX,targetY):
        super().__init__(x, y, vx, vy, radius, color)
        self.targetX = targetX
        self.targetY = targetY

    def updateVelforTarget(self): # 根据目标位置更新小球速度
        if self.targetX > self.x:
            self.vx = random.randint(1, 2)
        elif self.targetX < self.x:
            self.vx = random.randint(-2, -1)
        if self.targetY > self.y:
            self.vy = random.randint(1, 2)
        elif self.targetY < self.y:
            self.vy = random.randint(-2, -1)

balls = []  # 存储所有小球的信息，初始为空列表

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    hero.draw()  # 绘制玩家飞机
    for i in range(live): # 绘制还有几条生命
        livePics[i].draw()
    for ball in balls:
        ball.draw()   # 绘制小球
    screen.draw.text(str(time)+'秒', (270, 10), fontsize=50,
                     fontname='s', color='black')
    if live<=0:
        clock.unschedule(count)  # 结束函数的计划执行任务
        screen.draw.text("游戏结束！", (80, 300),
                         fontsize=100, fontname='s', color='red')

def update():  # 更新模块，每帧重复操作
    global live
    if live <=0: # 没有生命了，函数返回，不执行
        return

    for ball in balls:
        ball.update()  # 更新小球的位置、速度
        if abs(hero.x - ball.x) < 25 and abs(hero.y - ball.y) < 30:  # 玩家飞机和小球碰撞
            live -= 1 # 生命减1
            sounds.explode.play() # 爆炸一条命的音效
            ball.y = 10 # 当前小球立刻远离飞机，防止重复碰撞

    if live <= 0: # 生命减完了
        hero.image = 'blowup'  # 更换游戏玩家的图片为爆炸图片
        sounds.boom.play()  # 播放玩家飞机爆炸音效

def on_mouse_move(pos, rel, buttons):  # 当鼠标移动时执行
    if live > 0:  # 生命数大于0才执行
        hero.x = pos[0]  # 玩家飞机的x坐标设为鼠标的x坐标
        hero.y = pos[1]  # 玩家飞机的y坐标设为鼠标的y坐标

def count():
    global time
    time += 1 # 计时，每秒钟时间+1
    
    x = WIDTH//2   # 设为小球的x坐标
    y = random.randint(5, HEIGHT//10)   # 设为小球的y坐标
    vx = random.choice([-3, -2, -1, 1, 2, 3])  # 小球x方向的速度
    vy = random.randint(1, 3)  # 小球y方向的速度    

    # 每隔2秒，加一个小球，并且小球数目不超过20
    if time % 2 == 0 and len(balls) <= 20:
        r = 3      # 小球的半径
        color = 'black'  # 小球的颜色
        ball = Ball(x, y, vx, vy, r, color)  # 定义ball对象
        balls.append(ball)  # 把该小球的信息添加到balls中
        sounds.throw.play()

    # 当普通小球数目达到20个时，再加一种智能小球
    if time % 20 == 0 and len(balls) >= 10:
        r = 5      # 小球的半径
        color = 'red'  # 小球的颜色
        smartball = SmartBall(x, y, vx, vy, r, color,
                              hero.x, hero.y)  # 定义smartball对象
        balls.append(smartball)  # 把该小球的信息添加到balls中
        sounds.shakeeyes.play()

    for smartball in balls: # 每秒钟更新一次智能小球的速度
        if isinstance(smartball, SmartBall):  # 判断是智能小球对象
            smartball.targetX = hero.x  # 智能小球的目标
            smartball.targetY = hero.y
            smartball.updateVelforTarget() # 通过目标更新智能小球的速度           

    clock.schedule_unique(count, 1)  # 下一次隔1秒调用count()函数

count()  # 调用函数运行
pgzrun.go()   # 开始执行游戏
