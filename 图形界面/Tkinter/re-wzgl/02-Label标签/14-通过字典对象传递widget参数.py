import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, cnf={
    'width': 20,
    'height': 20,
    'fg': 'red',
    'bg': 'green'
})
label.pack()

root.mainloop()
