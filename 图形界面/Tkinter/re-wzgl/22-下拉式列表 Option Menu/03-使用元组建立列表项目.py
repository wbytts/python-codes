import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')

om_tuple = ("C", "Java", "Python")
var = tk.StringVar(root)
om = tk.OptionMenu(root, var, *om_tuple)
om.pack()

root.mainloop()
