"""
Message可以显示短消息，与Label类似，但是使用起来更灵活，可以自动分行

aspect：控件宽度与高度比，默认是 150%

"""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

msg = tk.Message(root, text="你好啊")
msg.pack()

root.mainloop()
