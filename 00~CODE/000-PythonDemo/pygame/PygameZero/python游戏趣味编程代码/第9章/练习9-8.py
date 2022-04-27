import pgzrun  # 导入游戏库
time = 0

def on_key_down():  # 当按下任意键盘键时执行
    print('程序已运行'+str(time)+'秒')

def count():
    global time
    time += 0.01
    clock.schedule_unique(count, 0.01)  # 下一次隔0.01秒调用

count()  # 调用函数运行
pgzrun.go()  # 开始执行游戏