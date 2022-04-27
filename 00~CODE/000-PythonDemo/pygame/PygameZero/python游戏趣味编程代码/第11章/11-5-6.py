import pgzrun  # 导入游戏库
import random  # 导入随机库
import copy # 导入复制库

TILE_SIZE = 50  # 小方块的大小，50*50
WIDTH = 10*TILE_SIZE  # 设置窗口的宽度 500
HEIGHT = 10*TILE_SIZE  # 设置窗口的高度 500

stars = []  # 二维数组，开始为空列表，用于储存小方块颜色编号
for i in range(10):  # 对行遍历
    row = []  # 存储一行的数据，开始为空列表
    for j in range(10):  # 对列遍历
        x = random.randint(1, 6) # 取1-6之间的随机数
        row.append(x)  # 把数据添加到行列表row中
    stars.append(row)  # 再把行列表row添加到二维数组stars中

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
     for k in range(20):  # 重复找多次，就可以把所有连通区域都找到了
        tempSet = copy.deepcopy(connectedSet) # 复制一份临时集合
        for each in tempSet: # 对集合中所有小方块处理
            i = each[0]  # 小方块对应的行序号
            j = each[1]  # 小方块对应的列序号
            #  找到上下左右四个方块，把颜色一致的添加到集合中，注意防止超过边界
            colorId = stars[i][j]
            if i > 0 and stars[i-1][j] == colorId:
                connectedSet.add((i-1, j))
            if i < 9 and stars[i+1][j] == colorId:
                connectedSet.add((i+1, j))
            if j > 0 and stars[i][j-1] == colorId:
                connectedSet.add((i, j-1))
            if j < 9 and stars[i][j+1] == colorId:
                connectedSet.add((i, j+1))
        tempSet.clear() # 临时集合清空

     for each in connectedSet:  # 对集合中的所有方块遍历
        stars[each[0]][each[1]] = 0  # 标记为0，对应黑色小方块图片

     updateTiles() # 根据stars更新Tiles二维数组

pgzrun.go()  # 开始执行游戏
