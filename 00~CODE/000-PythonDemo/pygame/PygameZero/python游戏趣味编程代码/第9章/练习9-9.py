import pgzrun  # 导入游戏库
time = 30

def draw():  # 绘制模块，每帧重复执行
    screen.fill('white')  # 白色背景
    screen.draw.text("倒计时："+str(time), (200, 80), fontsize=80,
                     fontname='s', color='black')
    if time<=0:  # 倒计时结束
        clock.unschedule(count)  # 结束函数的计划执行任务
        screen.draw.text("时间到了！", (180, 300),
                         fontsize=100, fontname='s', color='red')

def count():
    global time
    time -= 1
    clock.schedule_unique(count, 1)  # 下一次隔1秒调用

count()  # 调用函数运行
pgzrun.go()  # 开始执行游戏