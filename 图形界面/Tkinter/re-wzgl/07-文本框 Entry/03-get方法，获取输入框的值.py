import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

et = tk.Entry(root, width=30)
et.pack()

btn = tk.Button(root, text="按钮", command=lambda : print(et.get()))
btn.pack()

root.mainloop()
