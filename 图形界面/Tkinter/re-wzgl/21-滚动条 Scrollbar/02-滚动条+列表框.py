import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x300+0+0')

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lb = tk.Listbox(root, yscrollcommand=scrollbar.set)
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

for i in range(50):
    lb.insert(tk.END, "Line" + str(i))

scrollbar.config(command=lb.yview)

root.mainloop()
