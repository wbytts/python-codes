import pgzrun  # 导入游戏库

WIDTH = 350   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

background = Actor('background')  # 导入背景图片
bird = Actor('bird')  # 导入小鸟图片
bird.x = 50           # 设置小鸟的x坐标
bird.y = HEIGHT/2     # 设置小鸟的y坐标

def draw():   # 绘制模块，每帧重复执行
    background.draw()  # 绘制背景
    bird.draw()        # 绘制小鸟

def update():  # 更新模块，每帧重复操作
    bird.y = bird.y + 3 # 小鸟y坐标增加，即缓慢下落

pgzrun.go()   # 开始执行游戏