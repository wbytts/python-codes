import pgzrun
def draw():
    screen.fill('white')
    for r in range(250, 0, -50):
        screen.draw.filled_circle((400, 300), r, 'black')
        screen.draw.filled_circle((400, 300), r-25, 'white')
pgzrun.go()