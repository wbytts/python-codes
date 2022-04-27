import pgzrun
import random

balls = []
for i in range(100):
    x = random.randint(1,800)
    y = random.randint(1,600)
    ball = [x, y]
    balls.append(ball)

def draw():
    screen.fill('white')
    for ball in balls:
        screen.draw.filled_circle((ball[0], ball[1]), 10, 'red')

def update():
    global balls
    balls = []
    for i in range(100):
        x = random.randint(1, 800)
        y = random.randint(1, 600)
        ball = [x, y]
        balls.append(ball)

pgzrun.go()
