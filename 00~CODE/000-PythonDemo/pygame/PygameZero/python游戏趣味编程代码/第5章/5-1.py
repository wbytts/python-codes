import pgzrun  # 导入游戏库
WIDTH = 350   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

# 导入背景图片
background = Actor('background')

def draw():   # 绘制模块，每帧重复执行
    background.draw()  # 绘制背景图片

pgzrun.go()   # 开始执行游戏