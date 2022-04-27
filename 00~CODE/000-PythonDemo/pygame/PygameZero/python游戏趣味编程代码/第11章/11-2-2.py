import pgzrun  # 导入游戏库
import random  # 导入随机库

TILE_SIZE = 50  # 小方块的大小，50*50
WIDTH = 10*TILE_SIZE  # 设置窗口的宽度 500
HEIGHT = 10*TILE_SIZE  # 设置窗口的高度 500

stars = []  # 二维数组，开始为空列表，用于储存小方块颜色编号
for i in range(10):  # 对行遍历
    row = []  # 存储一行的数据，开始为空列表
    for j in range(10):  # 对列遍历
        x = random.randint(1, 6)  # 取1-6之间的随机数
        row.append(x)  # 把数据添加到行列表row中
    stars.append(row)  # 再行列表row添加到二维数组stars中

def draw():   # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    # 以下绘制出所有小方块的编号
    for i in range(10):
        for j in range(10):
            screen.draw.text(str(stars[i][j]),
                             (j*TILE_SIZE, i*TILE_SIZE), fontsize=35, color='white')

pgzrun.go()  # 开始执行游戏
