import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

v = tk.IntVar()

rb1 = tk.Radiobutton(root, text="男生", variable=v, value=1)
rb1.pack()

rb2 = tk.Radiobutton(root, text="女生", variable=v, value=0)
rb2.pack()


root.mainloop()
