import pgzrun  # 导入游戏库
WIDTH = 1200    # 设置窗口的宽度
HEIGHT = 600   # 设置窗口的高度

# 导入所有的分解动作图片，存在列表当中
Anims = [Actor('1'), Actor('2'), Actor('3'),
         Actor('4'), Actor('5')]
numAnims = len(Anims)  # 分解动作图片的张数
animIndex = 0  # 表示需要显示的动作图片的序号

player_x = WIDTH/2  # 设置玩家的x坐标
player_y = HEIGHT/2   # 设置玩家的y坐标
for i in range(numAnims):
    Anims[i].x = player_x  # 设置所有分解动作图片的x坐标
    Anims[i].y = player_y  # 设置所有分解动作图片的y坐标

def draw():    # 绘制模块，每帧重复执
    screen.fill('gray')  # 灰色背景
    Anims[animIndex].draw()  # 绘制玩家当前分解动作图片

def update():  # 更新模块，每帧重复操作
    global animIndex
    animIndex += 1  # 每一帧分解动作图片序号加1
    if animIndex >= numAnims:  # 放完最后一个分解动作图片了
        animIndex = 0  # 再变成第一张分解动作图片

pgzrun.go()  # 开始执行游戏