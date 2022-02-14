import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

frm1 = tk.Frame(width=250, height=50, bg="red")
frm1.pack()

frm2 = tk.Frame(width=250, height=50, bg="green")
frm2.pack()

frm3 = tk.Frame(width=250, height=50, bg="blue")
frm3.pack()

root.mainloop()
