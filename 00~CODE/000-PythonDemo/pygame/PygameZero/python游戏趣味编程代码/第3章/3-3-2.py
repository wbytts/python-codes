import pgzrun
def draw():
    screen.fill('white')
    for r in range(250, 0, -50):
        screen.draw.circle((400, 300), r, (255,0,0))
pgzrun.go()