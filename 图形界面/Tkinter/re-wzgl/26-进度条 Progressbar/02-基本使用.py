import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

pgb1 = ttk.Progressbar(root)
pgb1.pack(pady=20)
pgb1["maximum"] = 100
pgb1["value"] = 50

pgb2 = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode="determinate")
pgb2.pack(pady=20)
pgb2["maximum"] = 100
pgb2["value"] = 50

root.mainloop()
