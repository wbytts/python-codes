import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager



my_font = font_manager.FontProperties(fname='msyh.ttc')

plt.figure(figsize=(20, 8), dpi=80)

# 一天中每隔两个小时
x = range(2, 26, 2)
# 一天中每隔两小时的气温
y = [15, 13, 14, 5, 17, 20, 25, 26, 27, 22, 18, 15]

plt.bar(x, y)

plt.show()


