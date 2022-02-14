import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')

var = tk.StringVar()
cb = ttk.Combobox(root, textvariable=var, value=("C", "Java", "C#", "Go", "Python"))
# 选项放在外面设置可能更舒服一点
# cb["value"] = ("C", "Java", "C#", "Go", "Python")
cb.pack(pady=10)

root.mainloop()
