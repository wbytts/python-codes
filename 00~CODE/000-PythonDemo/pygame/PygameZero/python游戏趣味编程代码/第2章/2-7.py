import pgzrun
y = 100
def draw():
    screen.fill('white') 
    screen.draw.filled_circle((400, y), 30, 'red')
def update():
    global y
    y = y+1
pgzrun.go()
