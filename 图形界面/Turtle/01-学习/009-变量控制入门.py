import turtle as tt

tt.setup(600, 600, 0, 0)
tt.bgcolor('black')  # 背景颜色

pen = tt.Turtle()
pen.pencolor('white')  # 画笔颜色
pen.speed(0)

for i in range(200):
    # 距离和角度不同，展示的结果也不同
    '''
        次数  距离   度数
        240   i*2    200
        240   i*6    150
        360   i      100
        200   i*1.5  i
    '''
    pen.color('DeepSkyBlue', 'white')
    pen.forward(i * 1.5)
    pen.right(i)

tt.mainloop()
