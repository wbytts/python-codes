import pgzrun  # 导入游戏库
WIDTH = 480    # 设置窗口的宽度
HEIGHT = 700   # 设置窗口的高度

background1 = Actor('background')  # 导入背景图片
background1.x = 480/2  # 背景1的x坐标
background1.y = 852/2  # 背景1的y坐标
background2 = Actor('background')  # 导入背景图片
background2.x = 480/2   # 背景2的x坐标
background2.y = -852/2  # 背景2的y坐标

hero = Actor('hero')  # 导入玩家飞机图片
hero.x = WIDTH/2      # 设置玩家飞机的x坐标
hero.y = HEIGHT*2/3   # 设置玩家飞机的y坐标

def draw():  # 绘制模块，每帧重复执行
    background1.draw()  # 绘制游戏背景
    background2.draw()  # 绘制游戏背景
    hero.draw()  # 绘制玩家飞机

def update():  # 更新模块，每帧重复操作
    # 以下代码用于实现背景图片的循环滚动效果
    if background1.y > 852/2 + 852:
        background1.y = -852/2  # 背景1移动到背景2的正上方
    if background2.y > 852/2 + 852:
        background2.y = -852/2  # 背景2移动到背景1的正上方
    background1.y += 1  # 背景1向下滚动
    background2.y += 1  # 背景2向下滚动

def on_mouse_move(pos, rel, buttons):  # 当鼠标移动时执行
    hero.x = pos[0]  # 玩家飞机的x坐标设为鼠标的x坐标
    hero.y = pos[1]  # 玩家飞机的y坐标设为鼠标的y坐标

pgzrun.go()  # 开始执行游戏