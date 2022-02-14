import tkinter as tk
import tkinter.ttk as ttk
import random

root = tk.Tk()
root.geometry('300x210+0+0')

lb1 = tk.Listbox(root)
lb1.pack(side=tk.LEFT, padx=5, pady=10)


def add_item():
    # lb.insert(插入位置, 插入元素)
    # 插入位置如果是最后一个，可以写 tk.END
    lb1.insert(1, random.random())


btn = tk.Button(root, text="插入", command=add_item)
btn.pack(anchor=tk.N, side=tk.TOP, padx=5, pady=30)

root.mainloop()
