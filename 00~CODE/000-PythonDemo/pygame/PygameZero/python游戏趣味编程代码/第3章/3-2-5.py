import pgzrun
def draw():
    screen.fill('white')
    for r in range(10, 51, 10):
        screen.draw.circle((400, 300), r, 'black')
pgzrun.go()
