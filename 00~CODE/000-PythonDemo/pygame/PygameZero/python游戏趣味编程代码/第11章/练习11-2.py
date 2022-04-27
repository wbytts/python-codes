import pgzrun  # 导入游戏库
import random  # 导入随机库

TILE_SIZE = 20  # 小方块的大小，20*20
WIDTH = 30*TILE_SIZE  # 设置窗口的宽度 600
HEIGHT = 30*TILE_SIZE  # 设置窗口的高度 600

Cells = []  # 二维数组，开始为空列表，用于储存小方块编号
for i in range(30):  # 对行遍历
    row = []  # 存储一行的数据，开始为空列表
    for j in range(30):  # 对列遍历
        x = random.randint(0, 1)
        if i==0 or i==29 or j==0 or j==29:
            x = 0 # 边界处为0
        row.append(x)  # 把数据添加到行列表row中
    Cells.append(row)  # 再行列表row添加到二维数组Cells中

Tiles = []  # 二维数组，开始为空列表，存放所有小方块图片信息
def updateTiles():  # 根据Cells更新Tiles二维数组
    for i in range(30):
        for j in range(30):
            if Cells[i][j]==0:
                tile = Actor('die.jpg')  # 对应小方块图片初始化
            if Cells[i][j]==1:
                tile = Actor('live.jpg')  # 对应小方块图片初始化          
            tile.left = j * TILE_SIZE  # 小方块图片最左边的x坐标
            tile.top = i * TILE_SIZE  # 小方块图片最顶部的y坐标
            Tiles.append(tile)  # 将当前小方块加入到列表中

def draw():   # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in Tiles:
        tile.draw()  # 绘制所有小方块

def update():  # 更新模块，每帧重复操作
    global Cells
    NewCells = Cells  # 下一帧的细胞情况
    NeibourNumber = 0  # 统计临近细胞为生的个数
    for i in range(1,29):  # 对行遍历
        for j in range(1,29):  # 对列遍历
            NeibourNumber = Cells[i-1][j-1] + Cells[i-1][j] + Cells[i-1][j+1] \
                            + Cells[i][j-1] + Cells[i][j+1] \
                            + Cells[i+1][j-1] + Cells[i+1][j] + Cells[i+1][j+1]
            # 根据临近活着的细胞个数，统计下一帧对应的细胞状态
            if (NeibourNumber == 3):
                NewCells[i][j] = 1
            elif (NeibourNumber == 2):
                NewCells[i][j] = Cells[i][j]
            else:
                NewCells[i][j] = 0
    Cells = NewCells
    updateTiles()  # 根据Cells更新Tiles二维数组

pgzrun.go()  # 开始执行游戏