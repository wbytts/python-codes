import pgzrun

WIDTH = 800
HEIGHT = 400

def draw():
    screen.fill('white')  
    screen.draw.filled_circle((400, 400), 400, 'red')
    screen.draw.filled_circle((400, 400), 370, 'orange')
    screen.draw.filled_circle((400, 400), 340, 'yellow')
    screen.draw.filled_circle((400, 400), 310, 'green')
    screen.draw.filled_circle((400, 400), 280, 'blue')
    screen.draw.filled_circle((400, 400), 250, 'cyan')
    screen.draw.filled_circle((400, 400), 220, 'purple')
    screen.draw.filled_circle((400, 400), 190, 'white')

pgzrun.go()