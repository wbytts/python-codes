import pgzrun  # 导入游戏库

WIDTH = 600    # 设置窗口的宽度
HEIGHT = 800   # 设置窗口的高度
playerSpeed = 5 # 玩家水平移动速度

alien = Actor('alien')  # 导入玩家图片
alien.x = WIDTH/2      # 设置玩家的x坐标
alien.y = HEIGHT/2   # 设置玩家的y坐标

def draw():    # 绘制模块，每帧重复执行
    screen.clear()  # 清空游戏画面
    alien.draw()  # 绘制玩家

def update():  # 更新模块，每帧重复操作
    if keyboard.left: # 如果按下键盘左键
        alien.x = alien.x - playerSpeed  # 玩家左移
    if keyboard.right:  # 如果按下键盘右键
        alien.x = alien.x + playerSpeed  # 玩家右移

pgzrun.go()  # 开始执行游戏
