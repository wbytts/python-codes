import turtle as tt

pen = tt.Turtle()

for _ in range(4):
    # 往前画 100 像素
    pen.forward(100)
    # 右转 90 度
    pen.right(90)


tt.mainloop()
