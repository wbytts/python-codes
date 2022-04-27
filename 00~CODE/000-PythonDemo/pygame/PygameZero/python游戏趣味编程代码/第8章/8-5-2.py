import pgzrun  # 导入游戏库
import random  # 导入随机库

WIDTH = 600    # 设置窗口的宽度
HEIGHT = 800   # 设置窗口的高度
playerSpeed = 5 # 玩家水平移动速度

alien = Actor('alien')  # 导入玩家图片
alien.x = WIDTH/2      # 设置玩家的x坐标
alien.y = HEIGHT/5     # 设置玩家的y坐标

bricks = []  # 存储所有砖块的列表，开始为空
for i in range(5):
    brick = Actor('brick')  # 导入砖块图片
    brick.pos = 100*(i+1), 150*(i+1)    # 设置砖块的(x,y)坐标
    bricks.append(brick)  # 把当前砖块加入列表中

def draw():    # 绘制模块，每帧重复执行
    screen.clear()  # 清空游戏画面
    alien.draw()  # 绘制玩家
    for brick in bricks:  # 绘制列表中每个砖块
        brick.draw()  # 绘制砖块

def update():  # 更新模块，每帧重复操作
    isPlayerOnGround = False  # 开始假设角色没有站在砖块上
    for brick in bricks: # 对列表中所有砖块遍历
        # 玩家正好站在砖块上面，在方块左右之间，可以左右移动
        if abs(alien.bottom-brick.top) < 5  \
            and brick.left - alien.left < alien.width*2/3 \
            and alien.right - brick.right < alien.width*2/3:
            
            isPlayerOnGround = True  # 玩家在一块砖上
            alien.bottom = brick.top  # 玩家跟着砖块一直向上移动

            if keyboard.left:  # 如果按下键盘左键
                alien.x = alien.x - playerSpeed  # 玩家左移
            if keyboard.right:  # 如果按下键盘右键
                alien.x = alien.x + playerSpeed  # 玩家右移

    if not isPlayerOnGround:
        alien.y += 5  # 玩家不在任何一块砖上，就下落

    for birck in bricks: # 所有砖块缓慢上移
        birck.y -= 1

    if bricks[0].top < 10: # 最上面的一个砖块达到画面顶部时
        del bricks[0]  # 删除最上面的砖块
        brick = Actor('brick') # 新增一个砖块
        brick.x = random.randint(100, 500) # 水平位置随机
        brick.y = HEIGHT # 从最下部出现
        bricks.append(brick) # 将新砖块添加到列表中

pgzrun.go()  # 开始执行游戏
