import pgzrun


# 定义了一个绘图函数，说明具体的绘制工作
def draw():
    # 填充背景颜色
    screen.fill('green')
    # 绘制一个圆
    screen.draw.circle((400, 300), 100, 'white')
    # 绘制一个填充圆
    screen.draw.filled_circle((400, 300), 50, 'red')


# 让游戏开始运行
pgzrun.go()
