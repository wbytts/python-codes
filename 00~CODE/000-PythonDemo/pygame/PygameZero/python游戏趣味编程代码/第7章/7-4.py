import pgzrun  # 导入游戏库
import random  # 导入随机库

WIDTH = 480    # 设置窗口的宽度
HEIGHT = 700   # 设置窗口的高度

background1 = Actor('background')  # 导入背景1图片
background1.x = 480/2  # 背景1的x坐标
background1.y = 852/2  # 背景1的y坐标
background2 = Actor('background')  # 导入背景2图片
background2.x = 480/2   # 背景2的x坐标
background2.y = -852/2  # 背景2的y坐标

bullet = Actor('bullet')  # 导入子弹图片
bullet.x = WIDTH/2        # 子弹的x坐标
bullet.y = -HEIGHT       # 子弹的y坐标，开始不可见

hero = Actor('hero')  # 导入玩家飞机图片
hero.x = WIDTH/2      # 设置玩家飞机的x坐标
hero.y = HEIGHT*2/3   # 设置玩家飞机的y坐标

enemy = Actor('enemy')  # 导入敌机图片
enemy.x = WIDTH/2       # 设置敌机的x坐标
enemy.y = 0             # 设置敌机的y坐标

def draw():  # 绘制模块，每帧重复执行
    background1.draw()  # 绘制游戏背景
    background2.draw()  # 绘制游戏背景
    hero.draw()  # 绘制玩家飞机
    enemy.draw()  # 绘制敌机飞机
    bullet.draw()  # 绘制子弹

def update():  # 更新模块，每帧重复操作
    # 以下代码用于实现背景图片的循环滚动效果
    if background1.y > 852/2 + 852:
        background1.y = -852/2  # 背景1移动到背景2的正上方
    if background2.y > 852/2 + 852:
        background2.y = -852/2  # 背景2移动到背景1的正上方
    background1.y += 1  # 背景1向下滚动
    background2.y += 1  # 背景2向下滚动

    if bullet.y > -HEIGHT:
        bullet.y = bullet.y - 10 # 子弹自动向上移动

    enemy.y += 3 # 敌机自动下落
    if enemy.y > HEIGHT: # 敌机落到画面底部
        enemy.y = 0 # 敌机从上面重新出现
        enemy.x = random.randint(30, WIDTH-30)  # 敌机水平位置随机

def on_mouse_move(pos, rel, buttons):  # 当鼠标移动时执行
    hero.x = pos[0]  # 玩家飞机的x坐标设为鼠标的x坐标
    hero.y = pos[1]  # 玩家飞机的y坐标设为鼠标的y坐标

def on_mouse_down(): # 当鼠标键按下时
    bullet.x = hero.x   # 把子弹位置设为玩家飞机的正上方
    bullet.y = hero.y - 70

pgzrun.go()  # 开始执行游戏