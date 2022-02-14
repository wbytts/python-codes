import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="Hello World", bg="lightyellow")
label.place(x=300, y=400)

root.mainloop()
