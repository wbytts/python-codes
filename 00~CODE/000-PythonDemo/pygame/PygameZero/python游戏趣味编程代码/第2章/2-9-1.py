import pgzrun
y = 100
speed_y = 3

def draw():
    screen.fill('white') 
    screen.draw.filled_circle((400, y), 30, 'red')

def update():
    global y
    y = y+speed_y

pgzrun.go()