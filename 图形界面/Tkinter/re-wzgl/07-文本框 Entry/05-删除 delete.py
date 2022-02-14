import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

et = tk.Entry(root, width=30)
et.pack()

"""
delete(开始位置, 结束位置=None)

如果不指定结束位置，则默认为None，即最后
"""

def handle_click():
    et.insert(1, '#')


btn = tk.Button(root, text="按钮", command=handle_click)
btn.pack()

root.mainloop()
