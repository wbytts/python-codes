import pgzrun
R = 50
def draw():
    screen.fill('white')
    for x in range(R, 800, 2*R):
        screen.draw.filled_circle((x, 300), R, 'blue')
pgzrun.go()