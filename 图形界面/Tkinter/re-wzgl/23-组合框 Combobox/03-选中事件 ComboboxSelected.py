import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('250x60+0+0')


def cb_selection(event):
    lab_var.set(var.get())


var = tk.StringVar()
cb = ttk.Combobox(root, textvariable=var)
cb["value"] = ("C", "Java", "C#", "Go", "Python")
cb.pack(side=tk.LEFT, padx=10, pady=10)
cb.bind("<<ComboboxSelected>>", cb_selection)

lab_var = tk.StringVar()
lab = tk.Label(root, textvariable=lab_var)
lab_var.set(var.get())
lab.pack(side=tk.LEFT)

root.mainloop()
