"""
TopLevel：顶层窗口，所产生的的容器是一个独立的窗口

顶层窗口建立后
    如果关闭顶层窗口，主窗口仍然可以使用
    但是如果关闭了主窗口，程序将结束
"""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

tl = tk.Toplevel()
tl.title("Toplevel")


root.mainloop()
