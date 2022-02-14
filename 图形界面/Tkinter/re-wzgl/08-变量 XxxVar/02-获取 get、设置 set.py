import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

msg = tk.StringVar()

lab = tk.Label(root, textvariable=msg)
lab.pack()

et = tk.Entry(root, textvariable=msg)
et.pack()

btn_get = tk.Button(root, text="获取值")
btn_get.pack()

btn_set = tk.Button(root, text="设置值为###")
btn_set.pack()


def get_var_value(e):
    print(msg.get())


def set_var_value(e):
    msg.set('###')


btn_get.bind('<Button-1>', get_var_value)
btn_set.bind('<Button-1>', set_var_value)

root.mainloop()
