import pgzrun  # 导入游戏库

TILE_SIZE = 100  # 小拼图块的大小，100*100
WIDTH = 3*TILE_SIZE  # 设置窗口的宽度 300
HEIGHT = 3*TILE_SIZE  # 设置窗口的高度 300

# 导入9张图片文件，存在列表当中
tiles = [Actor('3×3_01'), Actor('3×3_02'), Actor('3×3_03'),
         Actor('3×3_04'), Actor('3×3_05'),Actor('3×3_06'),
         Actor('3×3_07'),Actor('3×3_08'),Actor('3×3_09')]

grid = [] # 列表，用来存放最终所有拼图信息
for i in range(3): # 对行循环
    for j in range(3): # 对列循环
        tile = tiles[i*3+j]  # 对应拼图方块图片
        tile.left = j * TILE_SIZE  # 拼图方块图片最左边的x坐标
        tile.top = i * TILE_SIZE  # 拼图方块图片最顶部的y坐标
        grid.append(tile) # 将当前拼图加入到列表中

# 以下实现两个小拼图块位置的交换
i = 0   # 第一个小拼图块的序号
j = 8   # 第二个小拼图块的序号
# 以下利用tempPos中间变量，实现两个小拼图块位置的交换
tempPos = grid[i].pos
grid[i].pos = grid[j].pos
grid[j].pos = tempPos


def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in grid:
        tile.draw()  # 绘制小拼图块

pgzrun.go()  # 开始执行游戏
