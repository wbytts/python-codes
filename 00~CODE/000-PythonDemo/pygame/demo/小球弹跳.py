import pygame
import os

WINDOW_W, WINDOW_H = 640, 480  # 窗体尺寸
FPS = 50  # 帧率，即每秒刷新多少次
g = 9.8 * 100  # 重力加速度（我们用的单位是像素每二次方秒）

pygame.init()  # 初始化pygame
# 设置窗口出现的位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,100)
# 创建一个窗口
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
# 设置窗口标题
pygame.display.set_caption("hello,world!")
# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

if __name__ == '__main__':
    x, y = WINDOW_W/2, 10   # 球的坐标
    vx, vy = 0, 0  # 球在x,y方向上的速度
    # 游戏主循环
    while True:
        # 遍历事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出事件后退出程序
                exit()

        # 小球下一时刻的速度、位置计算
        vy += g * 1/FPS
        x += vx * 1/FPS
        y += vy * 1/FPS
        if y >= WINDOW_H-10:
            # 到达地面则是其竖直速度反向
            vy = -vy

        # 将背景图画上去(0,0,0)为RGB颜色
        screen.fill((0, 0, 0))
        # 根据球的坐标画圆
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10)

        # 刷新画面
        pygame.display.update()
        # 设置FPS
        time_passed = clock.tick(FPS)
