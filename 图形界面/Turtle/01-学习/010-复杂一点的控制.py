import turtle as tt

tt.setup(600, 600, 0, 0)
tt.bgcolor('black')  # 背景颜色

pen = tt.Turtle()
pen.pencolor('white')  # 画笔颜色
pen.pensize(1)
pen.color('cyan')
pen.speed(0)

pen.up()
pen.goto(30, 120)
pen.down()
pen.ht()

c = 0
d = 0

while True:
    tt.tracer(2)
    for i in range(4):
        pen.forward(80)
        pen.right(90)
    pen.right(15)
    c += 1
    if c >= 24 + 2:
        pen.forward(60)
        c = 0
        d += 1
        if d >= 24 / 2:
            break


tt.mainloop()

