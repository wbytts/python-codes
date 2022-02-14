import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')

var = tk.StringVar(root)

# 预先设置 var 的值，可以建立默认选项
var.set("Java")

om = tk.OptionMenu(root, var, "C", "Java", "Python")
om.pack()


root.mainloop()
