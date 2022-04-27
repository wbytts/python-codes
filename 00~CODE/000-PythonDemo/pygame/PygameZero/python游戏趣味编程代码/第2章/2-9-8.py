import pgzrun
HEIGHT = 600
WIDTH = 800
y = 100
speed_y = 3
r = 30

def draw():
    screen.fill('white')  
    screen.draw.filled_circle((WIDTH/2, y), r, 'red')

def update():
    global y, speed_y
    y = y+speed_y
    if y >= HEIGHT-r or y <= r:
        speed_y = -speed_y

pgzrun.go()
