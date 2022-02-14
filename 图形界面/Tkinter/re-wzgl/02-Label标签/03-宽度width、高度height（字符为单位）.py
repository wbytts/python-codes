import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="Hello World",
                 fg="red", bg="blue",
                 # 注意，这里的宽度和高度指的都是字符为单位
                 height=3, width=15)
label.pack()

root.mainloop()
