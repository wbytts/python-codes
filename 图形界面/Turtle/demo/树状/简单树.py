import  turtle
import math

# def draw_line(p, x1, y1, x2, y2):
#     """画一条线段"""
#     p.penup()
#     p.goto(x1, y1)
#     p.pendown()
#     p.goto(x2, y2)
#     p.penup()

width = 800
height = 800
turtle.screensize(width, height)
pen = turtle.Turtle()

L = 100

pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.seth(90)
pen.forward(L)

pen.right(45)
pen.forward(L)


pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.setheading(90)
pen.forward(L)

pen.left(45)
pen.forward(L)

pen.position()

que = []
que.append({'x': 0, 'y': -100, 'angle': 90})





turtle.mainloop()




