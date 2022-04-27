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

Tiles = []  # 二维数组，开始为空列表，存放所有小方块图片信息
def updateTiles():  # 根据stars更新Tiles二维数组
    for i in range(10):
        for j in range(10):
            tile = Actor('star'+str(stars[i][j]))  # 对应小方块图片初始化
            tile.left = j * TILE_SIZE  # 小方块图片最左边的x坐标
            tile.top = i * TILE_SIZE  # 小方块图片最顶部的y坐标
            Tiles.append(tile)  # 将当前小方块加入到列表中
updateTiles()  # 根据stars更新Tiles二维数组

def draw():   # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in Tiles:
        tile.draw()  # 绘制所有小方块
    # 以下绘制出所有小方块的编号
    for i in range(10):
        for j in range(10):
            screen.draw.text(str(stars[i][j]),
                (j*TILE_SIZE, i*TILE_SIZE), fontsize=35, color='white')

def on_mouse_down(pos, button): # 当鼠标按键时执行
     iClicked = int(pos[1]/TILE_SIZE) # 点击方块在二维数组中的行序号
     jClicked = int(pos[0]/TILE_SIZE) # 点击方块在二维数组中的列序号
     connectedSet = {(iClicked, jClicked)}  # 创建集合，存储选中方块及其连通的点序号
    # 找到上下左右四个方块，把颜色一致的添加到集合中，注意防止超过边界
     colorId = stars[iClicked][jClicked]
     if iClicked > 0 and stars[iClicked-1][jClicked] == colorId:
        connectedSet.add((iClicked-1, jClicked))
     if iClicked < 9 and stars[iClicked+1][jClicked] == colorId:
        connectedSet.add((iClicked+1, jClicked))
     if jClicked > 0 and stars[iClicked][jClicked-1] == colorId:
        connectedSet.add((iClicked, jClicked-1))
     if jClicked < 9 and stars[iClicked][jClicked+1] == colorId:
        connectedSet.add((iClicked, jClicked+1))

     for each in connectedSet:  # 对集合中的所有方块遍历
        stars[each[0]][each[1]] = 0 # 标记为0，对应黑色小方块图片

     updateTiles() # 根据stars更新Tiles二维数组

pgzrun.go()  # 开始执行游戏
