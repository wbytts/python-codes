import turtle as tt

tt.setup(600, 600, 0, 0)
pen = tt.Turtle()

'''
speed -- 一个 0..10 范围内的整型数或速度字符串 (见下)
设置海龟移动的速度为 0..10 表示的整型数值。如未指定参数则返回当前速度。
如果输入数值大于 10 或小于 0.5 则速度设为 0。速度字符串与速度值的对应关系如下:

默认为 5

"fastest": 0 最快
"fast": 10 快
"normal": 6 正常
"slow": 3 慢
"slowest": 1 最慢

速度值从 1 到 10，画线和海龟转向的动画效果逐级加快。
注意: speed = 0 表示 没有 动画效果。forward/back 将使海龟向前/向后跳跃，同样的 left/right 将使海龟立即改变朝向。
'''
pen.speed(10)

pen.pencolor('blue')
pen.up()
pen.right(90)
pen.forward(150)
pen.left(90)
pen.down()
pen.circle(200)

tt.mainloop()
