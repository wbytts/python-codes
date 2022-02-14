from GUI.PyGame.game_colors import *

# pygame 程序的一些属性设置
TITLE = 'Jumpy!'  # pygame程序窗口标题
WIDTH = 480  # 游戏窗口的宽度
HEIGHT = 600  # 游戏窗口的高度
FPS = 60  # 游戏界面刷新率
FONT_NAME = 'arial' # 字体名称
BACKGROUND_COLOR = LIGHTBLUE  # 背景颜色
INFO_FILE = "info.txt"


# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# starting platforms
PLATFORM_LIST = [
    (0, HEIGHT - 40, WIDTH, 40),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
    (125, HEIGHT - 350, 100, 20),
    (350, 200, 100, 20),
    (175, 100, 50, 20)
]
