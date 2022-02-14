import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')


def handle_click():
    """通过 command 设置的点击方法，不需要接收事件对象"""
    print('点击了按钮')


btn = tk.Button(root, text="按钮", command=handle_click)
btn.pack()

root.mainloop()
