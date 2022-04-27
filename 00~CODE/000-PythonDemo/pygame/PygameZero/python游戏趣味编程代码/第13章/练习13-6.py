import pgzrun  # 导入游戏库
r = 4 # 白色小球半径
h_gray = r*2 # 灰色长条的高
# 两个白色小球之间的间隔、也是两个灰色长条间的间隔
step = r * 15
WIDTH = 12*step + 3*h_gray  # 设置窗口的宽度
HEIGHT = 8*step + 3*h_gray  # 设置窗口的高度

def draw():  # 绘制模块，每帧重复执行
    screen.fill('black') # 黑色背景
    # 画灰色长方形
    for i in range(h_gray, HEIGHT-h_gray, step):  # 画出水平的多个灰色长方形
        box = Rect((0, i), (WIDTH, h_gray))
        screen.draw.filled_rect(box, (150, 150, 150))
    for i in range(h_gray, WIDTH-h_gray, step):  # 画出竖直的多个灰色长方形
        box = Rect((i, 0), (h_gray, HEIGHT))
        screen.draw.filled_rect(box, (150, 150, 150))
    # 画白色小圆圈
    for i in range(h_gray, HEIGHT-h_gray, step):
        for j in range(h_gray, WIDTH-h_gray, step):
            screen.draw.filled_circle((j+r, i+r), h_gray, 'white')

pgzrun.go()  # 开始执行游戏