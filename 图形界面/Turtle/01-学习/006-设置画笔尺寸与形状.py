import turtle as tt

tt.setup(600, 600, 0, 0)
pen = tt.Turtle()

# 设置画笔的尺寸
pen.pensize(10)
# 设置画笔的形状
'''
常见的可选值：
    turtle   海龟
    square   正方形
    circle   圆形
'''
pen.shape('turtle')
# 设置海龟的大小
pen.turtlesize(2)

pen.pencolor('blue')
pen.up()
pen.right(90)
pen.forward(150)
pen.left(90)
pen.down()
pen.circle(200)

tt.mainloop()
