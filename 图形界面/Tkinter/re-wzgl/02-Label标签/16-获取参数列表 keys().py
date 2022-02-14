import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="Hello World")
label.pack()
print(label.keys())

root.mainloop()
