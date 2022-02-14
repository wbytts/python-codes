import turtle as tt
import math

tt.setup(600, 600, 0, 0)
pen = tt.Turtle()

# 设置背景颜色
tt.bgcolor('black')

# 用颜色的英文单词设置颜色
pen.pencolor('red')
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)

# RGB 方式设置颜色
pen.pencolor('#00FF00')
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)


# 颜色值三元组方式设置颜色
tt.colormode(255)  # 官方文档说，要先设置这个才行
pen.pencolor((0, 0, 255))
x, y = pen.pos()
pen.goto(x-100, y+100)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)

# color 同时设置填充颜色和画笔颜色，格式同 pencolor
# pen.color 和 turtle.color 好像有点区别
# pen(画笔颜色)  这种写法默认填充色也是画笔颜色
# pen(画笔颜色, 填充颜色)
pen.color('#FFFF00', '#00FFFF')
pen.left(45)
pen.circle(50 * math.sqrt(2))


tt.mainloop()
