import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

languages = ['C/C++', 'Java', 'Python']


def print_info():
    print(sp.get())


sp = tk.Spinbox(root,
                values=languages,
                wrap=True,
                command=print_info)
sp.pack(padx=10, pady=10)

root.mainloop()
