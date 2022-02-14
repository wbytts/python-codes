import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="Hello World")
# 组件.pack()
# 默认填充我们的窗口
label.pack()

root.mainloop()
