import turtle

width = 800
height = 800
turtle.screensize(width, height)
# 创建一支画笔
pen = turtle.Turtle()

# 按钮状态对象
btn = {'x': -400, 'y': 390, 'width': 100, 'height': 50}

def draw_button():
    """在左上角画一个按钮"""
    pen.up()  # 抬笔
    pen.goto(btn['x'], btn['y'])  # 找一个合适的画按钮的地方
    pen.down()  # 放下笔
    # 开始画按钮
    pen.forward(btn['width'])
    pen.right(90)
    pen.forward(btn['height'])
    pen.right(90)
    pen.forward(btn['width'])
    pen.right(90)
    pen.forward(btn['height'])


def handleClick(event):
    x, y = event.x, event.y
    print(f'鼠标左键在 ({x}, {y}) 处点击')
    # 判断点击位置是否在自己绘制出的按钮范围内，如果在，触发按钮点击事件


draw_button()
canvas = turtle.getcanvas()
canvas.bind('<Button-1>', handleClick)

# 保持窗口不关闭
turtle.mainloop()
