import pgzrun  # 导入游戏库
needles = []  # 存储所有针的列表，开始为空
# 导入针的图片、设置锚点相对坐标
newNeedle = Actor('needle', anchor=(170+50, 1))
newNeedle.x = 220     # 设置针锚点的x坐标
newNeedle.y = 300     # 设置针锚点的y坐标
needles.append(newNeedle)  # 初始一根针加入列表中

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    screen.draw.circle((400, 300), 80, 'red') # 绘制圆盘
    for needle in needles:  # 绘制列表中每根针
        needle.draw()        # 绘制针

def update():   # 更新模块，每帧重复操作
    for needle in needles:  # 对列表中每根针遍历处理
        if needle.x == 400:  # 如果针到了目标位置，才开始旋转
            needle.angle = needle.angle + 1  # 针的角度增加，即慢慢旋转

def on_key_down(): # 当按下任意键盘键时执行
    global newNeedle
    newNeedle.x = 400  # 针移动到目标位置

    # 再新建一根针
    newNeedle = Actor('needle', anchor=(170+50, 1))
    newNeedle.x = 220     # 设置针锚点的x坐标
    newNeedle.y = 300     # 设置针锚点的y坐标
    needles.append(newNeedle)  # 初始一根针加入列表中

pgzrun.go()   # 开始执行游戏