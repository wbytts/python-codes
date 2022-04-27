import pgzrun  # 导入游戏库

def draw():   # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    screen.draw.circle((400, 300), 80, 'red') # 绘制圆盘

pgzrun.go()   # 开始执行游戏
