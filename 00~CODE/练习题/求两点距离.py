import math

while True:
    x1 = input("x1=")
    y1 = input("y1=")
    x2 = input("x2=")
    y2 = input("y2=")

    if not all(map(lambda m: m.isdecimal(), [x1, x2, y1, y2])):
        print("你输入的坐标有误，请重新输入")
    else:
        x1, x2, y1, y2 = map(float, [x1, x2, y1, y2])
        print("两点间距离:", math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        break


