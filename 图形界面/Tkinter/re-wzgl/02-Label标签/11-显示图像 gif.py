import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

img = tk.PhotoImage(file="test.gif")

label = tk.Label(root, image=img)
label.pack()

root.mainloop()
