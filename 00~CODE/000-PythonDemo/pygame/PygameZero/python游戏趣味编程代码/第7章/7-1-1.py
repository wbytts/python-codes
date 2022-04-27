import pgzrun  # 导入游戏库
WIDTH = 480    # 设置窗口的宽度
HEIGHT = 852   # 设置窗口的高度

background = Actor('background')  # 导入背景图片
hero = Actor('hero')  # 导入玩家飞机图片
hero.x = WIDTH/2      # 设置玩家飞机的x坐标
hero.y = HEIGHT*2/3   # 设置玩家飞机的y坐标

def draw():
    background.draw()  # 绘制游戏背景
    hero.draw()  # 绘制玩家飞机

pgzrun.go()  # 开始执行游戏