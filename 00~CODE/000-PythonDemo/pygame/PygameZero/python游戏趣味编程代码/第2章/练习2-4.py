import pgzrun
r = 1
def draw():
    screen.fill('white') 
    screen.draw.filled_circle((400, 300), r, 'red')
def update():
    global r
    r = r+3
pgzrun.go()
