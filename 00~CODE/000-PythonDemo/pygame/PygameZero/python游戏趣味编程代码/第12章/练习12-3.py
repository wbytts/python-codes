import pgzrun  # 导入游戏库
WIDTH = 1200    # 设置窗口的宽度
HEIGHT = 900   # 设置窗口的高度

class Player(): # 定义玩家控制的角色类，带分解动画和移动功能
    Anims = []  # 所有的分解动作图片，存在列表当中
    numAnims = None  # 分解动作图片的张数
    animIndex = None  # 需要显示的动作图片的序号
    animSpeed = None  # 用于控制行走动画速度
    player_x = None  # 玩家的x坐标
    player_y = None   # 玩家的y坐标
    vx = None   # 玩家x方向的速度

    # 使用构造函数传递参数对对象初始化，分解动作图像列表，x,y坐标，x方向速度
    def __init__(self, Anims, player_x, player_y,vx):
        self.Anims = Anims
        self.numAnims = len(Anims)  # 分解动作图片的张数
        self.player_x = player_x  # 设置角色的x坐标
        self.player_y = player_y  # 设置角色的y坐标
        self.vx = vx             # 设置玩家x方向的速度
        self.animIndex = 0  # 需要显示的动作图片的序号
        self.animSpeed = 0  # 用于控制行走动画速度
        for i in range(self.numAnims):
            self.Anims[i].x = player_x  # 设置所有分解动作图片的x坐标
            self.Anims[i].y = player_y  # 设置所有分解动作图片的y坐标

    def draw(self):  # 绘制函数
        self.Anims[self.animIndex].draw()  # 绘制玩家当前分解动作图片

    def MoveRight(self):  # 向右移动时的一些操作
        self.player_x += self.vx  # 角色向右移动
        for i in range(self.numAnims):  # 所有分解动作图片更新x坐标
            self.Anims[i].x = self.player_x
        if (self.player_x >= WIDTH):  # 角色走到最右边
            self.player_x = 0  # 再从最左边出现
        self.animSpeed += 1  # 用于控制动作动画速度
        if self.animSpeed % 5 == 0:  # 动作动画速度是移动速度的1/5
            self.animIndex += 1  # 每一帧分解动作图片序号加1
            if self.animIndex >= self.numAnims:  # 放完最后一个分解动作图片了
                self.animIndex = 0  # 再变成第一张分解动作图片

# 定义两个Player对象，并初始化
# 两个角色的分解动作图片、初始位置、速度都不一样
player1 = Player([Actor('阿短1'), Actor('阿短2'), Actor('阿短3'),
                  Actor('阿短4'), Actor('阿短5')], WIDTH/10, HEIGHT/4, 5)
player2 = Player([Actor('小可1'), Actor('小可2'), Actor('小可3'),
                  Actor('小可4'), Actor('小可5')], WIDTH/10, 3*HEIGHT/4, 4)

def draw():    # 绘制模块，每帧重复执
    screen.fill('gray')  # 灰色背景
    player1.draw()  # 绘制角色1
    player2.draw()  # 绘制角色2

def update():  # 更新模块，每帧重复操作
    if keyboard.right:  # 如果按下键盘右键
        player1.MoveRight()    # 角色1向右移动
        player2.MoveRight()    # 角色2向右移动

pgzrun.go()  # 开始执行游戏