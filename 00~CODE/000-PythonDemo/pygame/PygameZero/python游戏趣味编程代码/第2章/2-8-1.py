import pgzrun
y = 100
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), 30, 'red')
def update():
    global y
    y = y+3
    if y>630:
        y = -30
pgzrun.go()
