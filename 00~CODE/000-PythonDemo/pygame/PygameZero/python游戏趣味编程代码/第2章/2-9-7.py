import pgzrun
y = 100
speed_y = 3

def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), 30, 'red')

def update():
    global y,speed_y
    y = y+speed_y
    if y>=570 or y<=30:
        speed_y = -speed_y

pgzrun.go()