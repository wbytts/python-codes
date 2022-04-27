import pgzrun  # 导入游戏库
import random  # 导入随机库
TILE_SIZE = 60  # 小拼图块的大小，60*60
WIDTH = 5*TILE_SIZE  # 设置窗口的宽度 300
HEIGHT = 5*TILE_SIZE  # 设置窗口的高度 300

clickTime = 0  # 记录鼠标点击了多少次
clickId1 = clickId2 = -1  # 两次点击的小拼图块的序号
allRight = False  # 是否小拼图的位置全对了

# 导入25张图片文件，存在列表当中
tiles = [Actor('5×5_01'), Actor('5×5_02'), Actor('5×5_03'), Actor('5×5_04'), Actor('5×5_05'),
         Actor('5×5_06'), Actor('5×5_07'), Actor('5×5_08'), Actor('5×5_09'), Actor('5×5_10'),
         Actor('5×5_11'), Actor('5×5_12'), Actor('5×5_13'), Actor('5×5_14'), Actor('5×5_15'),
         Actor('5×5_16'), Actor('5×5_17'), Actor('5×5_18'), Actor('5×5_19'), Actor('5×5_20'),
         Actor('5×5_21'), Actor('5×5_22'), Actor('5×5_23'), Actor('5×5_24'), Actor('5×5_25')]

grid = []  # 列表，用来存放最终所有拼图信息
for i in range(5):  # 对行循环
    for j in range(5):  # 对列循环
        tile = tiles[i*5+j]  # 对应拼图方块图片
        tile.left = j * TILE_SIZE  # 拼图方块图片最左边的x坐标
        tile.top = i * TILE_SIZE  # 拼图方块图片最顶部的y坐标
        grid.append(tile)  # 将当前拼图加入到列表中

# 以下函数实现两个小拼图块位置的交换
def swapPosition(i, j):
    # i，j为要交换的两个小拼图块的序号
    # 以下利用tempPos中间变量，实现两个小拼图块位置的交换
    tempPos = grid[i].pos
    grid[i].pos = grid[j].pos
    grid[j].pos = tempPos

# 重复随机交换多次小拼图的位置
for k in range(50):
    i = random.randint(0, 24)  # 第一个小拼图块的序号
    j = random.randint(0, 24)  # 第二个小拼图块的序号
    swapPosition(i, j)  # 调用函数交换两个小拼图块的位置

def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for tile in grid:
        tile.draw()  # 绘制小拼图块
    if allRight:  # 输出游戏胜利信息
        screen.draw.text("游戏胜利！", (40, HEIGHT/2-50),
                         fontsize=50, fontname='s', color='blue')
    else:  # 如果没有成功，可以画几条提示线
        for i in range(5):  # 画两条横线、两条竖线
            screen.draw.line((0, i*TILE_SIZE), (WIDTH, i*TILE_SIZE), 'white')
            screen.draw.line((i*TILE_SIZE, 0), (i*TILE_SIZE, HEIGHT), 'white')
        if clickId1 != -1:  # 为选中的第一个小拼图块画一个红色框
            screen.draw.rect(
                Rect((grid[clickId1].left, grid[clickId1].top), (TILE_SIZE, TILE_SIZE)), 'red')

def on_mouse_down(pos, button):  # 当鼠标按键时执行
    global clickTime, clickId1, clickId2, allRight
    for k in range(25):  # 对所有grid中的小拼图块遍历
        if grid[k].collidepoint(pos):  # 如果小拼图与鼠标位置碰撞
            print(k)  # 输出拼图块序号
            break    # 跳出当前循环

    if clickTime % 2 == 0:  # 点击偶数次
        clickId1 = k  # 第一个要交换的小拼图块序号
        clickTime += 1  # 点击次数加1
    elif clickTime % 2 == 1:  # 点击奇数次
        clickId2 = k  # 第二个要交换的小拼图块序号
        clickTime += 1  # 点击次数加1
        swapPosition(clickId1, clickId2)  # 交换两个小拼图块位置

    allRight = True  # 假设全拼对了
    for i in range(5):
        for j in range(5):
            tile = grid[i*5+j]
            # 遍历，只要有一个小拼图的位置不对，就没有全拼对
            if tile.left != j * TILE_SIZE or tile.top != i * TILE_SIZE:
                allRight = False  # 拼错了
                break
            # 如果上面的if语句都不执行，则表示全拼对了

pgzrun.go()  # 开始执行游戏