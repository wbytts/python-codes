import pygame as pg
from pygame.math import Vector2
import sys
import random

cell_size = 40
cell_number = 20


class Fruit:
    def __init__(self):
        self.randomize()

    def draw(self):
        fruit_rect = pg.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pg.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw(self):
        for block in self.body:
            rect = pg.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pg.draw.rect(screen, (183, 111, 122), rect)

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(len(self.body), body_copy[-1] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[1:]
            print(body_copy)
            body_copy.insert(len(self.body), body_copy[-1] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move()
        self.check_eat()
        self.check_fail()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def check_eat(self):
        if self.fruit.pos == self.snake.body[0]:
            print('吃到食物!', self.fruit.pos)
            # 重新设置水果位置，不能在蛇的身体上产生食物
            while self.fruit.pos in self.snake.body:
                self.fruit.randomize()
            # 增长蛇的身体
            self.snake.add_block()

    def check_fail(self):
        print(self.snake.body)
        # 检查超出屏幕
        if not 0 <= self.snake.body[-1].x < cell_number or not 0 <= self.snake.body[-1].y < cell_number:
            self.game_over('撞到屏幕，游戏结束')
        # 检查撞到自己
        for block in self.snake.body[:-1]:
            if block == self.snake.body[-1]:
                self.game_over('撞到自己， 游戏结束')

    def game_over(self, msg):
        print(msg)
        pg.quit()
        sys.exit()


pg.init()  # 初始化 pygame 程序
screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pg.time.Clock()  # 时钟

'''
Display surface: 显示表面，游戏的画布，只有一个，默认被显示
Surface: 用于显示，可以有多个，默认不显示
'''

game = Game()

pg.time.set_timer(pg.USEREVENT, 250)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # 退出 pygame 程序
            sys.exit()  # 退出应用程序
        if event.type == pg.USEREVENT:
            game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and game.snake.direction != Vector2(0, -1) and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN and game.snake.direction != Vector2(0, 1) and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pg.K_LEFT and game.snake.direction != Vector2(-1, 0) and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pg.K_RIGHT and game.snake.direction != Vector2(1, 0) and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)

    # 绘制我们的元素
    screen.fill((175, 215, 70))
    game.draw()
    pg.display.update()  # 更新显示
    clock.tick(60)  # 控制while循环每秒不超过60次
