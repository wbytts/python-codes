import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

nb = ttk.Notebook(root)
nb.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

nb.add(frame1, text="选项卡1")
nb.add(frame2, text="选项卡2")

root.mainloop()
