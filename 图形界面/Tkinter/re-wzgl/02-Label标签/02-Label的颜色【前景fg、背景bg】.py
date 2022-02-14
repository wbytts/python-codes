import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# foreground：前景色， 简写 fg
# backgruond：背景色， 简写 bg
label = tk.Label(root, text="啦啦啦", fg="red", bg="blue")
label.pack()

root.mainloop()

