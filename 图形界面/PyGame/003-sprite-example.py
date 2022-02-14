import pygame
import random

# 定义颜色元组
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800  # 游戏窗口的宽度
HEIGHT = 600  # 游戏窗口的高度
FPS = 30  # 游戏界面刷新率

# 初始化 pygame 和 创建窗口
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
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
