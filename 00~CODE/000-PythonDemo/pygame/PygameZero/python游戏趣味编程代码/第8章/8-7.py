import pgzrun  # 导入游戏库
import random  # 导入随机库

WIDTH = 600    # 设置窗口的宽度
HEIGHT = 800   # 设置窗口的高度
playerSpeed = 5  # 玩家水平移动速度
brickSpeed = 2   # 砖块自动上移速度
isLoose = False  # 游戏是否失败
score = 0     # 游戏得分

alien = Actor('alien')  # 导入玩家图片
alien.x = WIDTH/2      # 设置玩家的x坐标
alien.y = HEIGHT/5     # 设置玩家的y坐标
lastAlienY = alien.y  # 记录角色上一帧的y坐标

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
    screen.draw.text("你已坚持了 "+str(score)+"层！", (400, 20), fontsize=25,
                     fontname='s', color='white')
    if isLoose:  # 如果游戏失败，输出相关信息
        screen.draw.text("游戏失败！", (80, HEIGHT/2-100),
                         fontsize=100, fontname='s', color='red')

def update():  # 更新模块，每帧重复操作
    global isLoose, playerSpeed, brickSpeed, score, lastAlienY

    isPlayerOnGround = False  # 开始假设角色没有站在砖块上
    for brick in bricks: # 对列表中所有砖块遍历
        # 玩家正好站在砖块上面，在方块左右之间，可以左右移动
        if abs(alien.bottom-brick.top) < 5  \
            and brick.left - alien.left < alien.width*2/3 \
            and alien.right - brick.right < alien.width*2/3:
            alien.image = 'alien' # 设为在砖块上站立的图片
            isPlayerOnGround = True  # 玩家在一块砖上
            alien.bottom = brick.top  # 玩家跟着砖块一直向上移动
            if lastAlienY < alien.y:
                score += 1  # 之前还不在砖上，表示现在刚开始落到砖上，分数+1

            if keyboard.left:  # 如果按下键盘左键
                alien.x = alien.x - playerSpeed  # 玩家左移
            if keyboard.right:  # 如果按下键盘右键
                alien.x = alien.x + playerSpeed  # 玩家右移

    lastAlienY = alien.y  # 对所有砖块遍历后，更新lastAlienY的值

    if not isPlayerOnGround:
        alien.image = 'alien_falling'  # 设为在空中的玩家图片
        alien.y += 5  # 玩家不在任何一块砖上，就下落

    for birck in bricks: # 所有砖块缓慢上移
        birck.y -= brickSpeed

    if bricks[0].top < 10: # 最上面的一个砖块达到画面顶部时
        del bricks[0]  # 删除最上面的砖块
        brick = Actor('brick') # 新增一个砖块
        brick.x = random.randint(100, 500) # 水平位置随机
        brick.y = HEIGHT # 从最下部出现
        bricks.append(brick) # 将新砖块添加到列表中

    if alien.top < 0 or alien.bottom > HEIGHT:  # 角色超出上下范围，游戏失败
        playerSpeed = 0  # 玩家水平移动速度设为0
        brickSpeed = 0   # 砖块自动上移速度设为0
        isLoose = True   # 游戏失败

pgzrun.go()  # 开始执行游戏