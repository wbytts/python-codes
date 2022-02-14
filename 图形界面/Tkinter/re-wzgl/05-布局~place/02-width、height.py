import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="Hello World", bg="lightyellow")

# 可以直接通过 width、height 设定widget的实际大小
# 注：这里的 width 和 height 采用的是像素单位
label.place(x=300, y=400, width=20, height=20)

root.mainloop()
