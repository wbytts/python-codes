import pgzrun
def draw():
    screen.fill('white')
    for r in range(1, 6):
        screen.draw.circle((400, 300), 10*r, 'black')
pgzrun.go()
