import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

'''
字体设置：
    字形 family
    字号 size
    字重 weight
    斜体 slant
    下划线 underline
    上划线 overstrike
'''
label = tk.Label(root, text="Hello World",
                 fg="red", bg="skyblue",
                 width=20, height=10,
                 font="Helvetic 20 bold"
                 )
label.pack()

# 还可以写成元组的方式
label2 = tk.Label(root, text="Hello World",
                 fg="red", bg="skyblue",
                 width=20, height=10,
                 font=("Consolas", 24, "bold")
                 )
label2.pack()

root.mainloop()
