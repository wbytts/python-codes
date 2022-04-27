import pgzrun
import random
WIDTH = 1200
HEIGHT = 800
R = 100
def draw():
    screen.fill('white')
    for x in range(R, WIDTH, 2*R):
        for y in range(R, HEIGHT, 2*R):
             for r in range(1, R, 10):
                screen.draw.filled_circle((x, y), 100-r, \
                 (random.randint(0, 255), random.randint(0, 255),\
                 random.randint(0, 255)))
def on_mouse_down():
    draw()
pgzrun.go()