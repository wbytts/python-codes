import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('300x210+0+0')

lb1 = tk.Listbox(root)
lb1.pack(side=tk.LEFT, padx=5, pady=10)

lb2 = tk.Listbox(root, height=5, relief="raised")
lb2.pack(anchor=tk.N, side=tk.LEFT, padx=5, pady=10)

root.mainloop()
