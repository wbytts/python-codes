import pgzrun  # 导入游戏库
import time  # 导入时间库

TILE_SIZE = 20  # 小蛇方块的大小，20*20
WIDTH = 40*TILE_SIZE  # 设置窗口的宽度 800
HEIGHT = 30*TILE_SIZE  # 设置窗口的高度 600

snkaeHead = Actor('snake1')  # 导入蛇头方块图片
snkaeHead.x = WIDTH/2   # 蛇头方块图片的x坐标
snkaeHead.y = HEIGHT/2  # 蛇头方块图片的y坐标

Snake = []  # 存储蛇的列表
Snake.append(snkaeHead)  # 把蛇头加入到列表中

direction = 'up'  # 控制小蛇运动方向

for i in range(4):  # 再为蛇添加4段蛇身
    snakebody = Actor('snake1')  # 导入蛇身方块图片
    snakebody.x = Snake[i].x - TILE_SIZE  # 蛇身方块图片的x坐标
    snakebody.y = Snake[i].y  # 蛇身方块图片的y坐标
    Snake.append(snakebody)   # 把蛇身加入到列表中

def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for snkaebody in Snake:  # 绘制蛇
        snkaebody.draw()

def update():  # 更新模块，每帧重复操作
    newSnakeHead = Actor('snake1')  # 创建新蛇头的图片

    # 根据direction变量设定新蛇头的坐标，比如小蛇向下移动，就在旧蛇头的下边
    newSnakeHead = Actor('snake1')
    if direction == 'right':  # 小蛇向右移动
        newSnakeHead.x = Snake[0].x + TILE_SIZE
        newSnakeHead.y = Snake[0].y
    if direction == 'left':  # 小蛇向左移动
        newSnakeHead.x = Snake[0].x - TILE_SIZE
        newSnakeHead.y = Snake[0].y
    if direction == 'up':  # 小蛇向上移动
        newSnakeHead.x = Snake[0].x
        newSnakeHead.y = Snake[0].y - TILE_SIZE
    if direction == 'down':  # 小蛇向下移动
        newSnakeHead.x = Snake[0].x
        newSnakeHead.y = Snake[0].y + TILE_SIZE

    Snake.insert(0, newSnakeHead)  # 把新蛇头加到列表的最前面
    del Snake[len(Snake)-1]  # 删除掉旧蛇尾
    time.sleep(0.2)  # 暂停0.2秒

pgzrun.go()  # 开始执行游戏
