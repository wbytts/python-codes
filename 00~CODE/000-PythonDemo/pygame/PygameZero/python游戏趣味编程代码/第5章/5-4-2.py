import pgzrun  # 导入游戏库

WIDTH = 350   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

background = Actor('background')  # 导入背景图片
bird = Actor('bird')  # 导入小鸟图片
bird.x = 50           # 设置小鸟的x坐标
bird.y = HEIGHT/2     # 设置小鸟的y坐标
bar_up = Actor('bar_up')    # 导入障碍物上半部分图片
bar_up.x = 300              # 设置障碍物上半部分的x坐标
bar_up.y = 0           # 设置障碍物上半部分的y坐标
bar_down = Actor('bar_down')    # 导入障碍物下半部分图片
bar_down.x = 300                # 设置障碍物下半部分的x坐标
bar_down.y = 600             # 设置障碍物下半部分的y坐标

def draw():   # 绘制模块，每帧重复执行
    background.draw()  # 绘制背景
    bar_up.draw()      # 绘制障碍物上半部分
    bar_down.draw()    # 绘制障碍物下半部分
    bird.draw()        # 绘制小鸟

def update():  # 更新模块，每帧重复操作
    bird.y = bird.y + 2  # 小鸟y坐标增加，即缓慢下落
    bar_up.x = bar_up.x - 2   # 障碍物上半部分缓慢向左移动
    bar_down.x = bar_down.x - 2   # 障碍物下半部分缓慢向左移动

def on_mouse_down():  # 当鼠标点击时运行
    bird.y = bird.y - 100  # 小鸟y坐标减少，即上升一段距离

pgzrun.go()   # 开始执行游戏
