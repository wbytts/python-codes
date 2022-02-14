import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root, text="HelloWorld", bg="lightyellow")
label.pack(padx=100, pady=50)

root.mainloop()
