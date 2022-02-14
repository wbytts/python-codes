import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root)
label['width'] = 20
label['height'] = 20
label['fg'] = 'red'
label['bg'] = 'green'
label.pack()

root.mainloop()
