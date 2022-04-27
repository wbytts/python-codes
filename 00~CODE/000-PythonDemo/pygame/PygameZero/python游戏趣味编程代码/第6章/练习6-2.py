import pgzrun  # 导入游戏库

sun = Actor('太阳')  # 导入太阳图片
sun.x = 400    # 太阳x坐标
sun.y = 300    # 太阳y坐标

earth = Actor('地球', anchor=(65+250, 65))  # 导入地球图片
earth.x = 400    # 设置地球锚点的x坐标
earth.y = 300    # 设置地球锚点的y坐标

def draw():   # 绘制模块，每帧重复执行
    screen.fill('black')  # 黑色背景
    sun.draw()    # 绘制太阳
    earth.draw()  # 绘制地球

def update():   # 更新模块，每帧重复操作
    earth.angle = earth.angle + 1  # 地球的角度增加，慢慢旋转

pgzrun.go()   # 开始执行游戏