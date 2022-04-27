import pgzrun
X = [1,2,3,4,5,6]
def on_mouse_down():
    for x in X:
        if (x%3==0):
            return
        print(x)
pgzrun.go()