import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="HelloWorld", bg="lightyellow")
# 设置控件在窗口中的位置，取值参照label的 anchor
label.pack(anchor=tk.SE)

root.mainloop()
