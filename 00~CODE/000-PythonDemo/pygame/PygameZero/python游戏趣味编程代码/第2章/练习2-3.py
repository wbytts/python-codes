import pgzrun

def draw():
    screen.fill('white') 
    screen.draw.circle((400, 300), 250, 'black')
    screen.draw.circle((305, 180), 90, 'black')
    screen.draw.circle((495, 180), 90, 'black')
    screen.draw.filled_circle((275, 180), 55, 'black')
    screen.draw.filled_circle((465, 180), 55, 'black')
    screen.draw.circle((400, 300), 20, 'black')
    screen.draw.circle((400, 420), 70, 'black')

pgzrun.go()