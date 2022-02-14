import matplotlib.pyplot as plt


# 一天中每隔两个小时
x = range(2, 26, 2)
# 一天中每隔两小时的气温
y = [15, 13, 14, 5, 17, 20, 25, 26, 27, 22, 18, 15]

# h作为x轴，气温作为y轴，进行绘制折线图
plt.plot(x, y)
# 在执行程序时进行展示图形
plt.show()


