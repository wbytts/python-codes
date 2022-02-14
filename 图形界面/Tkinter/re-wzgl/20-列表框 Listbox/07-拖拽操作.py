"""
当 Listbox 的项被选取时，会产生 <<ListboxSelect>> 虚拟事件
"""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')


def get_index(event):
    lb.index = lb.nearest(event.y)


def drag_task(event):
    new_index = lb.nearest(event.y)
    if new_index == lb.index: return
    x = lb.get(new_index)
    lb.delete(new_index)
    lb.insert(new_index + (1 if new_index < lb.index else -1), x)
    lb.index = new_index


fruits = ["banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]
lab_var = tk.StringVar()
lab = tk.Label(root, text="", textvariable=lab_var)
lab.pack(pady=5)

lb = tk.Listbox(root)
lb.pack(pady=5)

for fruit in fruits:
    lb.insert(tk.END, fruit)
    lb.bind("<Button-1>", get_index)
    lb.bind("<B1-Motion>", drag_task)

root.mainloop()
