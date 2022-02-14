import matplotlib.pyplot as plt


"""
figure：图形图标的意思，在这里就是指我们要话的图
通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
在图像模糊的时候，可以传入dpi参数，使图像更加清晰
"""
plt.figure(figsize=(20, 8), dpi=80)

# 一天中每隔两个小时
x = range(2, 26, 2)
# 一天中每隔两小时的气温
y = [15, 13, 14, 5, 17, 20, 25, 26, 27, 22, 18, 15]

# h作为x轴，气温作为y轴，进行绘制折线图
plt.plot(x, y)
# 在执行程序时进行展示图形
plt.show()


