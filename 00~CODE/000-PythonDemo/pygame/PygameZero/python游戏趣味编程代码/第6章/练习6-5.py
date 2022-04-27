import pgzrun  # 导入游戏库

sun = Actor('太阳')  # 导入太阳图片
sun.x = 400    # 太阳x坐标
sun.y = 300    # 太阳y坐标

earth = Actor('地球', anchor=(65+250, 65))  # 导入地球图片
earth.x = 400    # 设置地球锚点的x坐标
earth.y = 300    # 设置地球锚点的y坐标
rotateSpeed = 1  # 地球旋转速度初始化为1

def draw():   # 绘制模块，每帧重复执行
    screen.fill('black')  # 黑色背景
    sun.draw()    # 绘制太阳
    earth.draw()  # 绘制地球

def update():   # 更新模块，每帧重复操作
    earth.angle = earth.angle + rotateSpeed  # 地球的角度增加rotateSpeed

def on_key_down():  # 当按下任意键盘键时执行
    global rotateSpeed
    if (rotateSpeed == 1):   # 之前旋转，现在暂停
        rotateSpeed = 0
    elif (rotateSpeed == 0): # 之前暂停，现在旋转
        rotateSpeed = 1

pgzrun.go()   # 开始执行游戏