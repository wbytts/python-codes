import pgzrun

WIDTH = 800
HEIGHT = 400

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'cyan', 'purple', 'white']

def draw():
    screen.fill('white')  
    for r in range(8):
        screen.draw.filled_circle((400, 400), 400-r*30, colors[r])

pgzrun.go()