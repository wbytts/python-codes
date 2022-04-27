import pgzrun
import random

WIDTH = 800
HEIGHT = 600

x = WIDTH / 2
y = HEIGHT / 2

speed_x = 3
speed_y = 5

r = 1

# 定义了一个绘图函数，说明具体的绘制工作
def draw():
    # 填充背景颜色
    # screen.fill('white')
    # 绘制一个填充圆

    random_r = int(random.random() * 255)
    random_g = int(random.random() * 255)
    random_b = int(random.random() * 255)

    screen.draw.filled_circle((x, y), r, (random_r, random_g, random_b))



def update():
    global x, y, speed_x, speed_y
    x = x + speed_x
    y = y + speed_y
    if x >= WIDTH - r or x <= r:
        speed_x = -speed_x
    if y >= HEIGHT - r or y <= r:
        speed_y = - speed_y

    # screen.draw.filled_circle((x, y), 5, 'green')


# 让游戏开始运行
pgzrun.go()


