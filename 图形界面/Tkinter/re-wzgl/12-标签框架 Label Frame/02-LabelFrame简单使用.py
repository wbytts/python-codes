import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

frm1 = tk.LabelFrame(root, tex="这是 LabelFrame", width=250, height=100, borderwidth=1, relief=tk.SOLID)
frm1.pack()


btn1 = tk.Button(frm1, text="按钮1")
btn1.place(x=0, y=0)



root.mainloop()
