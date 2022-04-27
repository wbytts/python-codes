import pgzrun  # 导入游戏库
import time  # 导入时间库
import random # 导入随机库

TILE_SIZE = 20  # 小蛇方块的大小，20*20
WIDTH = 40*TILE_SIZE  # 设置窗口的宽度 800
HEIGHT = 30*TILE_SIZE  # 设置窗口的高度 600

snkaeHead = Actor('snake1')  # 导入蛇头方块图片
snkaeHead.x = WIDTH/2   # 蛇头方块图片的x坐标
snkaeHead.y = HEIGHT/2  # 蛇头方块图片的y坐标

cookie = Actor('cookie')  # 导入食物方块图片
cookie.x = random.randint(10, 30)*TILE_SIZE  # 食物方块图片的x坐标
cookie.y = random.randint(10, 30)*TILE_SIZE  # 食物方块图片的y坐标


Snake = []  # 存储蛇的列表
Snake.append(snkaeHead)  # 把蛇头加入到列表中

direction = 'up'  # 控制小蛇运动方向

isLoose = False # 游戏是否失败

for i in range(4):  # 再为蛇添加4段蛇身
    snakebody = Actor('snake1')  # 导入蛇身方块图片
    snakebody.x = Snake[i].x - TILE_SIZE  # 蛇身方块图片的x坐标
    snakebody.y = Snake[i].y  # 蛇身方块图片的y坐标
    Snake.append(snakebody)   # 把蛇身加入到列表中

def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    for snkaebody in Snake:  # 绘制蛇
        snkaebody.draw()
    cookie.draw() # 食物的绘制
    if isLoose:  # 显示游戏失败信息
        screen.draw.text("游戏失败！", (180, HEIGHT/2-100),
                         fontsize=100, fontname='fangz', color='blue')

def update():  # 更新模块，每帧重复操作
    global direction,isLoose
    if keyboard.left:  # 如果按下键盘左键
        direction = 'left'  # 小蛇要向左移
    if keyboard.right:  # 如果按下键盘右键
        direction = 'right'  # 小蛇要向右移
    if keyboard.up:  # 如果按下键盘上键
        direction = 'up'  # 小蛇要向上移
    if keyboard.down:  # 如果按下键盘下键
        direction = 'down'  # 小蛇要向下移

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

    # 当小蛇（新蛇头）超出边框时游戏失败
    if newSnakeHead.y < 0 or newSnakeHead.y > HEIGHT \
        or newSnakeHead.x < 0 or newSnakeHead.x > WIDTH:
        isLoose = True

    # 当小蛇蛇头碰到自身时，游戏失败
    for snakebody in Snake: # 对所有蛇身循环，判断是否和蛇头坐标一致
        if newSnakeHead.x == snakebody.x and newSnakeHead.y == snakebody.y:
            isLoose = True
            break

    # 当小蛇头碰到食物时，不处理，也就是长度+1；饼干重新随机位置出现；
    if newSnakeHead.x == cookie.x and newSnakeHead.y == cookie.y:
        cookie.x = random.randint(5, 35)*TILE_SIZE
        cookie.y = random.randint(5, 25)*TILE_SIZE
    else:  # 否则，删除掉旧蛇尾，也就是蛇的长度保持不变
        del Snake[len(Snake)-1]

    Snake.insert(0, newSnakeHead)  # 把新蛇头加到列表的最前面
    time.sleep(0.2)  # 暂停0.2秒

pgzrun.go()  # 开始执行游戏
