import pgzrun  # 导入游戏库
num = 0

def output():
    global num
    num += 1
    print(num)
    clock.schedule_unique(output, 1)  # 下一次隔1秒调用

output() # 调用函数运行
pgzrun.go()  # 开始执行游戏