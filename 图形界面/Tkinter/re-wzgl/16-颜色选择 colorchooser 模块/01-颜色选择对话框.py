import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser

root = tk.Tk()
root.geometry('800x600+0+0')


def get_color():
    # ((89.34765625, 139.54296875, 232.90625), '#598be8')
    # 返回值是一个元组，第一个是三原色数值的元组，第二个是十六进制字符串形式
    c = colorchooser.askcolor()
    print(c)


btn = tk.Button(root, text="选择颜色", command=get_color)
btn.pack()

root.mainloop()
