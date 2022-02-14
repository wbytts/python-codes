import pygame as pg
import random
import os
from p005.settings import *
from game_colors import *
from p005.sprites import Player


# 设置游戏资源文件夹为当前文件所在文件夹
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Game:
    def __init__(self):
        # 初始化游戏窗口，游戏设置 - initialize game
        self.playing = False
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # 开始一个新游戏 - start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()  # 运行游戏

    def run(self):
        # 游戏循环 - game loop
        self.playing = True  # 标识当前是否在进行游戏
        while self.playing:
            self.clock.tick(FPS)  # 游戏时钟
            self.events()  # 游戏事件处理
            self.update()  # 游戏状态更新
            self.draw()  # 游戏界面绘制

    def events(self):
        # 游戏循环 - 事件处理 - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        # 游戏循环 - 更新 - update
        self.all_sprites.update()

    def draw(self):
        # 游戏循环 - 绘制 - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # 游戏启动界面 - game splash/start screen
        pass

    def show_go_screen(self):
        # 游戏结束界面 - game over/continue
        pass


g = Game()  # 创建游戏类实例
g.show_start_screen()  # 显示游戏启动界面
# 游戏循环
while g.running:
    g.new()  # 开始一个新游戏
    g.show_go_screen()  # 显示游戏结束界面

pg.quit()  # 退出pygame程序
