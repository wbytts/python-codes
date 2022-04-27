import pgzrun
r = 100
def draw():
    screen.fill('white')  
    screen.draw.filled_circle((150, 300), r, 'red')
    screen.draw.filled_circle((400, 300), r, 'yellow')
    screen.draw.filled_circle((650, 300), r, 'blue')
pgzrun.go()
