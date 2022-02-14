import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

yscroll = tk.Scrollbar(root)
text = tk.Text(root, width=30, height=5)
yscroll.pack(side=tk.RIGHT, fill=tk.Y)
text.pack()

yscroll.config(command=text.yview)
text.config(yscrollcommand=yscroll.set)

text.insert(tk.END, "Hello World" * 100)

root.mainloop()
