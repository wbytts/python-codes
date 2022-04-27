import pgzrun  # 导入游戏库

# 导入初始位置针的图片、设置锚点相对坐标
startNeedle = Actor('needle', anchor=(170+50, 1))
startNeedle.x = 200     # 设置针锚点的x坐标
startNeedle.y = 300     # 设置针锚点的y坐标
needles = []  # 存储所有针的列表，开始为空

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    startNeedle.draw()    # 初始位置针的绘制
    for needle in needles:  # 绘制列表中每根针
        needle.draw()        # 绘制针
    screen.draw.filled_circle((400, 300), 80, 'red')  # 绘制圆盘

def update():   # 更新模块，每帧重复操作
    for needle in needles:  # 对列表中每根针遍历处理
        needle.angle = needle.angle + 1  # 针的角度增加，即慢慢旋转

def on_key_down(): # 当按下任意键盘键时执行
    # 再新建一根针
    newNeedle = Actor('needle', anchor=(170+50, 1))
    newNeedle.x = 400     # 设置针锚点的x坐标
    newNeedle.y = 300     # 设置针锚点的y坐标

    for needle in needles:
        if newNeedle.colliderect(needle):
            print('游戏失败')

    needles.append(newNeedle)  # 把针加入列表中

pgzrun.go()   # 开始执行游戏
