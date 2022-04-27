import pgzrun
WIDTH = 800
HEIGHT = 600
x = WIDTH/2
y = HEIGHT/2
speed_x = 3
speed_y = 5
r = 30

def draw():
    screen.fill('white') 
    screen.draw.filled_circle((x, y), r, 'red')

def update():
    global x,y,speed_x,speed_y
    x = x+speed_x
    y = y+speed_y
    if x >= WIDTH-r or x <= r:
        speed_x = -speed_x
    if y >= HEIGHT-r or y <= r:
        speed_y = -speed_y

pgzrun.go()