import pygame  # 导入pygame库
from pygame.locals import *  # 导入一些常用的函数和常量
from sys import exit  # 向sys模块借一个exit函数用来退出程序

pygame.init()  # 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((640, 480), 0, 32)  # 创建了一个窗口
pygame.display.set_caption("Hello, World!")  # 设置窗口标题

while True:  # 游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            exit()
    pygame.display.update()  # 刷新一下画面
