#from turtle import *
import turtle as tt

tt.pensize(5)

tt.goto(200, 0)
tt.goto(200, 200)
tt.goto(0, 200)
tt.goto(0, 0)

tt.penup()
tt.goto(100, 100)
tt.pendown()

tt.goto(100, -100)
tt.goto(-100, -100)
tt.goto(-100, 100)
tt.goto(100, 100)

tt.penup()
tt.goto(-100, 100)
tt.pendown()
tt.goto(0, 200)

tt.penup()
tt.goto(100, 100)
tt.pendown()
tt.goto(200, 200)

tt.penup()
tt.goto(-100, -100)
tt.pendown()
tt.goto(0, 0)

tt.penup()
tt.goto(100, -100)
tt.pendown()
tt.goto(200, 0)

tt.done()

