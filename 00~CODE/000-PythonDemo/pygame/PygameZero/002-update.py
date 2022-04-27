import pgzrun

r = 100
m = 1

# 定义了一个绘图函数，说明具体的绘制工作
def draw():
    # 填充背景颜色
    screen.fill('green')
    # 绘制一个圆
    screen.draw.circle((400, 300), r, 'black')
    # 绘制一个填充圆
    screen.draw.filled_circle((400, 300), 50, 'red')


# 更新函数，和 draw 一样，每一帧都会重复运行的
def update():
    global r, m
    r += m
    if r >= 300 or r <= 50:
        m = -m

# 让游戏开始运行
pgzrun.go()

