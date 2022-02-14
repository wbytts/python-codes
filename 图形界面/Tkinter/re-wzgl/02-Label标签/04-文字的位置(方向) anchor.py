import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

"""
Anchor 方向：小写字符串，或者大写的常数 如 tk.NW
    上北下南左西右东
        nw      n       ne

        w     center    e

        sw      s       se
"""

label = tk.Label(root, text="Hello World",
                 fg="red", bg="skyblue",
                 width=20, height=20,
                 anchor="se"
                 )
label.pack()


root.mainloop()
