import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

"""
相同列的控件，如果宽度不同，grid方法会保留最宽的作为基准，这个时候比较短的就会居中对齐

sticky的功能类似anchor，可以设置 N、S、W、E
    组合使用：
        N+S：拉长高度让控件在顶端和底端对齐
        W+E：拉长宽度让控件在左边和右边对齐
        N+S+E：拉长高度让控件在顶端和底端对齐，同时切齐右边
        N+S+W：拉长高度让控件在顶端和底端对齐，同时切齐左边
        N+S+W+E：拉长高度让控件在顶端和低段对齐，同时切齐左边和右边



"""

root.mainloop()
