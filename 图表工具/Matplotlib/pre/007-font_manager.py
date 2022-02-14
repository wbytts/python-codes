import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='D:/projects/Python/PythonLearn/图表/Matplotlib/pre/msyh.ttc')

plt.figure(figsize=(20, 8), dpi=80)

# 一天中每隔两个小时
x = range(2, 26, 2)
# 一天中每隔两小时的气温
y = [15, 13, 14, 5, 17, 20, 25, 26, 27, 22, 18, 15]

# h作为x轴，气温作为y轴，进行绘制折线图
plt.plot(x, y)

# 设置x轴的刻度
_x_labels = ['{} 时'.format(i) for i in x]
plt.xticks(x, _x_labels, rotation=90, fontproperties=my_font)

# 保存图片
# 可以保存为 .svg 这种矢量图，放大不会有锯齿
plt.savefig('./pic.png')

# 在执行程序时进行展示图形
plt.show()
