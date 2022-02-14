"""
当 Listbox 的项被选取时，会产生 <<ListboxSelect>> 虚拟事件
"""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')


def item_select(event):
    obj = event.widget
    index = obj.curselection()
    lab_var.set(obj.get(index))


fruits = ["banana", "Watermelon", "Pineapple", "Orange", "Grapes", "Mango"]
lab_var = tk.StringVar()
lab = tk.Label(root, text="", textvariable=lab_var)
lab.pack(pady=5)

lb = tk.Listbox(root)
lb.pack(pady=5)

for fruit in fruits:
    lb.insert(tk.END, fruit)

# 如果想要双击触发，也可以绑定 <Double-Button-1> 的事件
lb.bind("<<ListboxSelect>>", item_select)

root.mainloop()
