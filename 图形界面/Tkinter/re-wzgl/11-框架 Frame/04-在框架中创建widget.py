import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

frm1 = tk.Frame(width=250, height=50, borderwidth=1, relief=tk.SOLID)
frm1.pack()

frm2 = tk.Frame(width=250, height=50, borderwidth=1, relief=tk.SOLID)
frm2.pack()


btn1 = tk.Button(frm1, text="按钮1")
btn1.place(x=0, y=0)

btn2 = tk.Button(frm2, text="按钮2")
btn2.place(x=0, y=0)


root.mainloop()
