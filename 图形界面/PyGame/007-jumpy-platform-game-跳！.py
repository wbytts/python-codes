import pygame as pg
import random
import os
from p007.sprites import *
import json

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
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # 初始化游戏数据
        self.dir = os.path.dirname(__file__)
        try:
            with open(os.path.join(self.dir, INFO_FILE), 'r') as f:
                s = f.read()
                self.data = json.loads(s)
        except:
            self.data = {'high_score': 0}

    def new(self):
        # 开始一个新游戏 - start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        # 游戏循环 - 更新 - update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        # if play reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()  # 不见了的 platform 就杀掉，节省内存
                    self.score += 10
        # spawn new platforms to keep same average number
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platforms) == 0:
            self.playing = False

    def draw(self):
        # 游戏循环 - 绘制 - draw
        self.screen.fill(BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()

    def show_start_screen(self):
        # 游戏启动界面 - game splash/start screen
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text('Arrows to move, Space to Jump', 20, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text('Press a key to play', 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text('High Score: ' + str(self.data['high_score']), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # 游戏结束界面 - game over/continue
        if not self.running:
            return
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_text('GAME OVER', 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text('Score: ' + str(self.score), 20, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text('Press a key to play again', 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        # 保存当前最高分
        if self.score > self.data['high_score']:
            self.data['high_score'] = self.score
            self.draw_text('NEW HIGH SCORE!', 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(os.path.join(self.dir, INFO_FILE), 'w') as f:
                data_str = json.dumps(self.data)
                f.write(data_str)
        else:
            self.draw_text('High Score: ' + str(self.data['high_score']), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()  # 创建游戏类实例
g.show_start_screen()  # 显示游戏启动界面
# 游戏循环
while g.running:
    g.new()  # 开始一个新游戏
    g.show_go_screen()  # 显示游戏结束界面

pg.quit()  # 退出pygame程序
