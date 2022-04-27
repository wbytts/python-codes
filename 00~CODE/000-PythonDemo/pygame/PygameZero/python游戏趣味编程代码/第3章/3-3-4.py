import pgzrun
def draw():
    screen.fill('white')
    for r in range(250, 0, -50):
        screen.draw.filled_circle((400, 300), r, (r, 0, 0))
pgzrun.go()