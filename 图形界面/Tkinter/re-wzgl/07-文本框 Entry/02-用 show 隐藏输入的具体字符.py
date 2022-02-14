import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

et = tk.Entry(root, width=30, show='*')
et.pack()

root.mainloop()
