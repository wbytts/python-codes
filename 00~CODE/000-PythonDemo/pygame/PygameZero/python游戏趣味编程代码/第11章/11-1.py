import pgzrun  # 导入游戏库
import random  # 导入随机库

TILE_SIZE = 50  # 小方块的大小，50*50
WIDTH = 10*TILE_SIZE  # 设置窗口的宽度 500
HEIGHT = 10*TILE_SIZE  # 设置窗口的高度 500

grid = []  # 列表，用来存放最终所有小方块的信息
for i in range(10):
    for j in range(10):
        x = random.randint(1, 6) # 小方块图片序号
        tile = Actor('star'+str(x))  # 对应小方块图片文件初始化
        tile.left = j * TILE_SIZE  # 小方块图片最左边的x坐标
        tile.top = i * TILE_SIZE  # 小方块图片最顶部的y坐标
        grid.append(tile)  # 将当前小方块加入到列表中

def draw():   # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in grid:
        tile.draw()  # 绘制所有小方块

pgzrun.go()  # 开始执行游戏