import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

et = tk.Entry(root, width=30)
et.pack()

"""
insert(位置, 字符串)
在指定位置插入指定字符串，原位置的字符后移
"""

def handle_click():
    et.insert(1, '#')


btn = tk.Button(root, text="按钮", command=handle_click)
btn.pack()

root.mainloop()
