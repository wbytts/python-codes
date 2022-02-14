import turtle as tt

# 可用，不过不知道为啥检测不到
tt.setup(600, 600, 0, 0)

# 命名一只画笔
pen = tt.Turtle()

for i in range(0, 100, 4):
    for _ in range(4):
        # 往前画 100 像素
        pen.forward(100+i)
        # 右转 90 度
        pen.right(90)


tt.mainloop()
