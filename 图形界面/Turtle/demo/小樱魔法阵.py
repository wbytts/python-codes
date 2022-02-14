import turtle as tt


def tcyuan(x, y, r):
    tt.fillcolor("black")
    tt.begin_fill()
    tt.seth(0)
    y = y - r
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.circle(r)
    tt.end_fill()


def yuan(x, y, r):
    tt.seth(0)
    y = y - r
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.circle(r)


def yueliang():
    R = 110 - 1

    r = R - 22 - 1

    # 月亮填充
    tt.penup()
    tt.goto(-350 + 2 * R, 0)
    tt.seth(90)
    tt.fillcolor("black")
    tt.begin_fill()
    tt.circle(R, 359)
    tt.left(90)
    tt.fd(2)
    tt.left(90)
    tt.circle(-r, 359)
    tt.left(90)
    tt.fd(2)
    tt.pendown()
    tt.end_fill()
    # 轮廓
    yuan(-350 + R, 0, R)
    yuan(-350 + 44 + r - 2, 0, r - 2)


def zhixian(R, r, count, jiaodu):
    tt.seth(90 + jiaodu)
    #    tt.goto(0, 0)
    for i in range(count):
        tt.penup()
        tt.goto(0, 0)
        tt.fd(r)
        tt.pendown()
        tt.fd(R - r)
        tt.left(360 / count)


def zfx(R, r):
    jiange = 10
    #    tt.pensize(jiange)
    tt.seth(90)
    big = pow((R ** 2) * 2, 0.5)
    small = big - 2 * jiange
    for i in range(13):
        # 大线
        tt.penup()
        tt.goto(0, 0)
        tt.fd(R)
        tt.pendown()
        tt.right(135)
        tt.fd(big)
        # 小线
        tt.left(135)
        tt.penup()
        tt.goto(0, 0)
        tt.fd(pow((small ** 2) / 2, 0.5))
        tt.pendown()
        tt.right(135)
        tt.fd(small)
        # 粗线
        tt.pensize(8)
        tt.pencolor("black")
        tt.left(135)
        tt.penup()
        tt.goto(0, 0)
        tt.fd((R + pow((small ** 2) / 2, 0.5)) / 2)
        tt.pendown()
        tt.right(135)
        tt.fd((big + small) / 2)
        tt.pensize(2)
        tt.pencolor("yellow")
        tt.seth(90 + i * 30)
    else:
        # 大线
        tt.penup()
        tt.goto(0, 0)
        tt.fd(R)
        tt.right(135)
        tt.fd(big / 2)
        tt.pendown()
        tt.fd(big / 2)
        # 小线
        tt.left(135)
        tt.penup()
        tt.goto(0, 0)
        tt.fd(pow((small ** 2) / 2, 0.5))
        tt.right(135)
        tt.fd(small / 2)
        tt.pendown()
        tt.fd(small / 2)
        # 粗线
        tt.pensize(8)
        tt.pencolor("black")
        tt.left(135)
        tt.penup()
        tt.goto(0, 0)
        tt.fd((R + pow((small ** 2) / 2, 0.5)) / 2)
        tt.right(135)
        tt.fd((big + small) / 2 / 2)
        tt.pendown()
        tt.fd((big + small) / 2 / 2)
        tt.pensize(2)
        tt.pencolor("yellow")
        tt.seth(90 + i * 30)


def wjx(r, jiaodu):
    tt.fillcolor("black")
    tt.penup()
    tt.goto(0, 0)
    tt.seth(90 + jiaodu)
    tt.fd(r)
    tt.pendown()
    tt.right(18)
    tt.begin_fill()
    for i in range(5):
        tt.right(144)
        tt.forward(144)
        tt.left(72)
        tt.forward(144)
    tt.end_fill()
    if jiaodu != 0:
        tt.seth(90 + jiaodu)
        for i in range(1, 6):
            tt.penup()
            tt.goto(0, 0)
            tt.left(72)
            tt.pendown()
            tt.fd(r)


def xingzuo():
    r = 250
    tt.penup()
    tt.goto(20, -35)
    tt.seth(-45)
    tt.fd(r)
    tt.pendown()
    xz = ['♒', '♓', '♈', '♉', '♌', '♍', '♎', '♏']
    for i in range(4):
        tt.write(xz[i], font=("", 20, ""))
        tt.penup()
        tt.right(90)
        tt.circle(-300, 30)
        tt.left(90)
        tt.pendown()
    tt.penup()
    tt.goto(-r / 4 + 10, 5)
    tt.seth(135)
    tt.fd(r)
    for i in range(4, 8):
        tt.write(xz[i], font=("", 20, ""))
        tt.penup()
        tt.right(90)
        tt.circle(-300, 30)
        tt.left(90)
        tt.pendown()


def dxnb(s):
    tt.penup()
    tt.fd(-19)
    tt.left(90)
    tt.fd(2)
    tt.pendown()
    tt.write(s, font=["KaiTi", 30, "bold"])


def taiyang():
    def haicao(r, i):
        # 海藻
        tt.fillcolor("black")

        tt.penup()
        if i == 0:
            tt.goto(256, r)
        elif i == 1:
            tt.goto(256 - r, 0)
        else:
            tt.goto(256, -r)
        tt.pendown()
        tt.begin_fill()
        tt.seth(2 + i * 90)
        tt.circle(r / 2, 105)
        tt.left(10)
        tt.circle(-r / 3, 90)
        tt.circle(r / 3, 60)
        tt.left(20)
        tt.circle(r / 3, -80)
        tt.left(50)
        tt.circle(-r + 10, -40)
        tt.right(30)
        tt.circle(r / 2 + 10, -50)
        tt.penup()
        if i == 0:
            tt.goto(256, r)
        elif i == 1:
            tt.goto(256 - r, 0)
        else:
            tt.goto(256, -r)
        tt.pendown()
        tt.end_fill()

        tt.seth(2 + i * 90)
        tt.circle(r / 2, 105)
        tt.left(10)
        tt.circle(-r / 3, 90)
        tt.begin_fill()
        tt.circle(r / 3, 60)
        tt.left(20)
        tt.circle(r / 3, -80)
        tt.left(50)
        tt.circle(-r + 10, -40)
        tt.right(30)
        tt.circle(r / 2 + 10, -50)
        tt.right(30)
        tt.circle(r / 2 - 2, 110)
        tt.circle(-r / 3, 70)
        tt.left(7)
        tt.circle(r / 3, 85)
        tt.end_fill()

        tt.penup()
        if i == 0:
            tt.goto(256, r)
            tt.pendown()
            tt.seth(180 - (2 + i * 90))
            tt.circle(-(r / 2), 105)
        elif i == 1:
            tt.goto(256 - r, 0)
            tt.pendown()
            tt.seth(- (2 + i * 90))
            tt.circle(-(r / 2), 105)
        else:
            tt.goto(256, -r)
            tt.pendown()
            tt.seth(180 - (2 + i * 90))
            tt.circle(-(r / 2), 105)
        tt.begin_fill()
        tt.left(-10)
        tt.circle(-(-r / 3), 90)
        tt.circle(-(r / 3), 60)
        tt.left(-20)
        tt.circle(-(r / 3), -80)
        tt.left(-50)
        tt.circle(-(-r + 10), -40)
        tt.right(-30)
        tt.circle(-(r / 2 + 10), -50)
        tt.end_fill()

        tt.penup()
        if i == 0:
            tt.goto(256, r)
            tt.pendown()
            tt.seth(180 - (2 + i * 90))
            tt.circle(-(r / 2), 105)
        elif i == 1:
            tt.goto(256 - r, 0)
            tt.pendown()
            tt.seth(- (2 + i * 90))
            tt.circle(-(r / 2), 105)
        else:
            tt.goto(256, -r)
            tt.pendown()
            tt.seth(180 - (2 + i * 90))
            tt.circle(-(r / 2), 105)
        tt.pendown()

        tt.left(-10)
        tt.circle(-(-r / 3), 90)
        tt.circle(-(r / 3), 60)
        tt.left(-20)
        tt.begin_fill()
        tt.circle(-(r / 3), -80)
        tt.left(-50)
        tt.circle(-(-r + 10), -40)
        tt.right(-30)
        tt.circle(-(r / 2 + 10), -50)
        tt.right(-30)
        tt.circle(-(r / 2 - 2), 110)
        tt.circle(-(-r / 3), 70)
        tt.left(-7)
        tt.circle(-(r / 3), 85)
        tt.end_fill()

    def xhaicao(r, i):
        tt.penup()
        tt.goto(256 + r, 0)
        tt.seth(-90)
        tt.circle(-r, 20)
        tt.pendown()
        tt.begin_fill()
        tt.seth(30)
        tt.circle(-r / 3, 100)
        tt.circle(r / 6, 140)
        tt.circle(-r / 11, 100)
        tt.left(80)
        tt.circle(-r / 2, -30)
        tt.circle(r / 4, -140)
        tt.circle(-r / 3, -60)
        tt.end_fill()
        tt.penup()
        tt.goto(256 + r, 0)
        tt.seth(-90)
        tt.circle(-r, 30)
        tt.pendown()
        tt.seth(45)
        tt.circle(-r / 4, 100)
        tt.right(20)
        tt.circle(r / 4, 140)
        tt.right(10)
        tt.circle(-r / 11, 90)

        tt.penup()
        tt.goto(256 + r, 0)
        tt.seth(90)
        tt.circle(r, 20)
        tt.pendown()
        tt.begin_fill()
        tt.seth(-30)
        tt.circle(-(-r / 3), 100)
        tt.circle(-(r / 6), 140)
        tt.circle(-(-r / 11), 100)
        tt.left(-80)
        tt.circle(-(-r / 2), -30)
        tt.circle(-(r / 4), -140)
        tt.circle(-(-r / 3), -60)
        tt.end_fill()
        tt.penup()
        tt.goto(256 + r, 0)
        tt.seth(90)
        tt.circle(r, 30)
        tt.pendown()
        tt.seth(-45)
        tt.circle(-(-r / 4), 100)
        tt.right(-25)
        tt.circle(-(r / 4), 140)
        tt.right(-10)
        tt.circle(-(-r / 11), 90)

    r = 50
    # 海藻
    haicao(r, 0)
    haicao(r, 1)
    haicao(r, 2)
    xhaicao(r, 3)

    # 大三角形
    tt.fillcolor("black")

    for i in range(1, 4):
        temp = 3
        tt.penup()
        tt.goto(256, 0)
        tt.seth(i * 90)
        tt.pendown()
        tt.begin_fill()
        tt.right(22.5)
        tt.fd(r)
        if i == 1:
            tt.goto(256, 3 * r - temp)
            tt.goto(256, 0)
            tt.seth(i * 90 + 22.5)
            tt.fd(r)
            tt.goto(256, 3 * r - temp)
        elif i == 2:
            tt.goto(256 - 3 * r + temp, 0)
            tt.goto(256, 0)
            tt.seth(i * 90 + 22.5)
            tt.fd(r)
            tt.goto(256 - 3 * r + temp, 0)
        else:
            tt.goto(256, -3 * r + temp)
            tt.goto(256, 0)
            tt.seth(i * 90 + 22.5)
            tt.fd(r)
            tt.goto(256, -3 * r + temp)
        tt.end_fill()
    # 小三角形
    x = pow(((2 * r) ** 2) / 2, 0.5) - 8
    for i in range(1, 5):
        tt.penup()
        tt.goto(256, 0)
        tt.seth(i * 90)
        tt.pendown()
        tt.begin_fill()
        tt.right(22.5)
        tt.fd(r)
        if i == 1:
            tt.goto(256 + x, x)
            tt.goto(256, 0)
            tt.right(45)
            tt.fd(r)
            tt.goto(256 + x, x)
        elif i == 2:
            tt.goto(256 - x, x)
            tt.goto(256, 0)
            tt.right(45)
            tt.fd(r)
            tt.goto(256 - x, x)
        elif i == 3:
            tt.goto(256 - x, -x)
            tt.goto(256, 0)
            tt.right(45)
            tt.fd(r)
            tt.goto(256 - x, -x)
        else:
            tt.goto(256 + x, -x)
            tt.goto(256, 0)
            tt.right(45)
            tt.fd(r)
            tt.goto(256 + x, -x)
        tt.end_fill()

    # 圆
    #    tt.begin_fill()
    tcyuan(256, 0, r)


# 初始化
tt.setup(1500, 800, 0, 0)
tt.speed(0)
tt.bgcolor("black")
tt.pencolor("yellow")
tt.pensize(2)
# 最大的圆
yuan(0, 0, 350)
yuan(0, 0, 325)
yuan(0, 0, 321)
yuan(0, 0, 306)
zhixian(321, 306, 72, 0)
# 小圆
yuan(0, 0, 204)
yuan(0, 0, 200)
yuan(0, 0, 186)
zhixian(200, 186, 72, 0)
# 正方形边框以及直线
zhixian(290, 213, 12, 0)
zhixian(248, 205, 12, 15)
zfx(306, 204)
# 里五角星
wjx(200, 36)
# 月亮
yueliang()
# 太阳
taiyang()
# 最小圆
tcyuan(0, 328, 22)
dxnb("北")
tcyuan(0, -328, 22)
dxnb("南")
tcyuan(-328, 0, 22)
dxnb("西")
tcyuan(328, 0, 22)
dxnb("東")

# 外五角星
wjx(200, 0)
# 星座
xingzuo()
tt.penup()
tt.goto(-500, -500)
tt.pendown()
tt.done()
