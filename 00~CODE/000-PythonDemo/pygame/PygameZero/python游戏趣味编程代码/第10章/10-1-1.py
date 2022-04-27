import pgzrun  # 导入游戏库

TILE_SIZE = 100  # 小拼图块的大小，100*100
WIDTH = 3*TILE_SIZE  # 设置窗口的宽度 300
HEIGHT = 3*TILE_SIZE  # 设置窗口的高度 300

tile = Actor('3×3_01')  # 导入拼图方块图片
tile.x = WIDTH/2   # 拼图方块图片的x坐标
tile.y = HEIGHT/2  # 拼图方块图片的y坐标

def draw():  # 绘制模块，每帧重复执行
    screen.clear()  # 每帧清除屏幕，便于重新绘制
    tile.draw()  # 绘制小拼图块

pgzrun.go()  # 开始执行游戏
