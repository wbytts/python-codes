import pygame
import random
import os
from game_colors import *

TITLE = 'My Game'
WIDTH = 800  # 游戏窗口的宽度
HEIGHT = 600  # 游戏窗口的高度
FPS = 30  # 游戏界面刷新率

# 设置游戏资源文件夹为当前文件所在文件夹
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

# 初始化 pygame 和 创建窗口
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        # self.image = pygame.image.load(os.path.join(img_folder, 'azhu.jpg')).convert()
        self.image.set_colorkey(BLACK)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 游戏循环
running = True
while running:
    # 让游戏循环以指定的速度运行
    clock.tick(FPS)
    # 处理输入、事件 process input / event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查窗口关闭事件
            running = False  # 退出游戏循环
    # 更新游戏状态 update
    all_sprites.update()
    # 绘制 draw、渲染 render
    screen.fill(BLACK)  # 整个屏幕填充黑色
    all_sprites.draw(screen)
    # 绘制完所有东西后，交换缓冲区显示
    pygame.display.flip()

pygame.quit()  # 退出游戏
