import pgzrun
def draw():
    screen.fill('white')
    for r in range(255, 0, -1):
        screen.draw.filled_circle((400, 300), r, (r, r, r))
pgzrun.go()
