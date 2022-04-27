import pgzrun  # 导入游戏库
needle = Actor('needle')  # 导入针的图片
needle.x = 100     # 设置针的x坐标
needle.y = 300     # 设置针的y坐标

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    screen.draw.circle((400, 300), 80, 'red') # 绘制圆盘
    needle.draw()        # 绘制针

def update():   # 更新模块，每帧重复操作
    needle.angle = needle.angle + 1  # 针的角度增加，即慢慢旋转

pgzrun.go()   # 开始执行游戏