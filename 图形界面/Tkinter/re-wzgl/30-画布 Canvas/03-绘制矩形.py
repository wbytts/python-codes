import tkinter as tk
import tkinter.ttk as ttk
import math
import random

root = tk.Tk()

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

"""
create_rectangle(x1, y1, x2, y2, options)
options选项：
    dash、dashoffset：建立虚线
    fill：矩形填充颜色
    outline：矩形线条颜色
    stipple：绘制位图矩形
    width：矩形线条宽度
"""

# for i in range(50):
#     x1, y1 = random.randint(1, 640), random.randint(1, 480)
#     x2, y2 = random.randint(1, 640), random.randint(1, 480)
#     if x1 > x2: x1, x2 = x2, x1
#     if y1 > y2: y1, y2 = y2, y1
#     canvas.create_rectangle(x1, y1, x2, y2)


def draw_task():
    def ddd():
        x1, y1 = random.randint(1, 640), random.randint(1, 480)
        x2, y2 = random.randint(1, 640), random.randint(1, 480)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        canvas.create_rectangle(x1, y1, x2, y2)
        canvas.after(100, ddd)
    ddd()

draw_task()

root.mainloop()
