import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('400x300+0+0')

lab = tk.Label(root, text="请选择你喜欢的编程语言:")
lab.grid(row=0)

var1 = tk.IntVar()
cb1 = tk.Checkbutton(root, text="C/C++", variable=var1)
cb1.grid(row=1, sticky=tk.W)

var2 = tk.IntVar()
cb2 = tk.Checkbutton(root, text="Java", variable=var2)
cb2.grid(row=2, sticky=tk.W)

var3 = tk.IntVar()
cb3 = tk.Checkbutton(root, text="Python", variable=var3)
cb3.grid(row=3, sticky=tk.W)

root.mainloop()
