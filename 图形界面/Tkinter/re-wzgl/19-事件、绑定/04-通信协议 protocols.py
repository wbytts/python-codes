"""
Protocols 可以翻译为通信协议
在tkinter里可以解释为窗口管理程序与应用程序之间的通信协议
tkinter支持使用绑定概念更改此通信协议
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry('800x600+0+0')


def callback():
    res = messagebox.askokcancel('OKCANCEL', '结束或取消?')
    if res == True:
        root.destroy()
    else:
        return


# 更改协议绑定
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()
