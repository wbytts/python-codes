import tkinter as tk
import tkinter.ttk as ttk
import math

root = tk.Tk()

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# canvas.create_line(x1, y1, x2, y2, x3, y3, ..., xn, yn, options)
"""
options选项：
    arrow：默认没有箭头，FIRST在起始端有箭头，LAST在末端有箭头，BOTH在两端有箭头
    arrowshape：使用元组 (d1, d2, d3) 代表箭头，默认是 (8, 10, 3)
    capstyle：线条终点的样式，默认是 BUTT，可选 PROJECTING、ROUND
    dash：建立虚线，使用元组存储数字数据，第一个数字是实线，第二个数字是空白，以此类推，用完了从头开始
    dashoffset：与dash一样产生虚线，不过一开始是空白的宽度
    fill：设置线条颜色
    joinstyle：线条相交的设置，默认是 ROUND、可选 BEVEL、MITER
    stipple：绘制位图(Bitmap)线条
    width：线条宽度
"""

x_center, y_center, r = 320, 240, 100
x, y = [], []

for i in range(12):
    x.append(x_center + r * math.cos(30 * i * math.pi / 180))
    y.append(y_center + r * math.sin(30 * i * math.pi / 180))

for i in range(12):
    for j in range(12):
        canvas.create_line(x[i], y[i], x[j], y[j])

root.mainloop()
