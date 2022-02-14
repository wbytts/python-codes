import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# compound
"""
left：图片在左
right：图片在右
top：图片在上
bottom：图片在下
center：文字覆盖在图片上方
"""
label = tk.Label(root, text="Hello World", bitmap="hourglass",
                 compound="left")
label.pack()

root.mainloop()
