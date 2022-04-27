import pgzrun  # 导入游戏库

TILE_SIZE = 100  # 小拼图块的大小，100*100
WIDTH = 3*TILE_SIZE  # 设置窗口的宽度 300
HEIGHT = 3*TILE_SIZE  # 设置窗口的高度 300

grid = [] # 列表，用来存放最终所有拼图信息
for i in range(3): # 对行循环
    for j in range(3): # 对列循环
        tile = Actor('3×3_01')  # 导入拼图方块图片
        tile.left = j * TILE_SIZE # 拼图方块图片最左边的x坐标
        tile.top = i * TILE_SIZE  # 拼图方块图片最顶部的y坐标
        grid.append(tile) # 将当前拼图加入到列表中

def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in grid:
        tile.draw()  # 绘制小拼图块

pgzrun.go()  # 开始执行游戏
