import pgzrun
import random
def draw():
    screen.fill('white')
    for r in range(250, 0, -10):
        screen.draw.filled_circle((400, 300), r,\
        (random.randint(0, 255), random.randint(0, 255),\
        random.randint(0, 255)))
def on_mouse_down():
    draw()
pgzrun.go()