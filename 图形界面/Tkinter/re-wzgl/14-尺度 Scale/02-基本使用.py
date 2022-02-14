import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('300x200+0+0')

lab_var = tk.StringVar()
lab = tk.Label(root, textvariable=lab_var)
lab.pack()

scale1 = tk.Scale(root, variable=lab_var, orient=tk.HORIZONTAL)
scale1.pack()

scale2 = tk.Scale(root, variable=lab_var, orient=tk.VERTICAL)
scale2.pack()

root.mainloop()
