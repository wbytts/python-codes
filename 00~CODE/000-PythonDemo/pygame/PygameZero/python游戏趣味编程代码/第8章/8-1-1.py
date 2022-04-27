
import pgzrun  # 导入游戏库

WIDTH = 600    # 设置窗口的宽度
HEIGHT = 800   # 设置窗口的高度

alien = Actor('alien')  # 导入玩家图片
alien.x = WIDTH/2      # 设置玩家的x坐标
alien.y = HEIGHT/2   # 设置玩家的y坐标

def draw():    # 绘制模块，每帧重复执行
    screen.clear()  # 清空游戏画面
    alien.draw()  # 绘制玩家

pgzrun.go()  # 开始执行游戏
