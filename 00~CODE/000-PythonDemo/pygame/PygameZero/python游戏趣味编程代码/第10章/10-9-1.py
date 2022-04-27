import datetime
start = datetime.datetime.now()
a = input('按回车键后统计程序运行时间')
end = datetime.datetime.now()
time = (end - start).seconds
print('程序一共运行', time, '秒')
