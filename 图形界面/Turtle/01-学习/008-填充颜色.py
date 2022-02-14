import turtle as tt

tt.setup(600, 600, 0, 0)
pen = tt.Turtle()
pen.fillcolor('red')
pen.pensize(10)

pen.begin_fill()  # 开始填充
pen.circle(100)
pen.end_fill()  # 结束填充

# 如果图形没有闭合，则会将起点终点连起来填充

tt.mainloop()
