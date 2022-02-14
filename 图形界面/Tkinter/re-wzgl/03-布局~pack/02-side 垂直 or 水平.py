import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')
"""
side取值：
    TOP：默认，从上往下排列
    BOTTOM：从下往上排列
    LEFT：从左往右排列
    RIGHT：从右往左排列
"""
label1 = tk.Label(root, text="Hello1", bg="lightyellow")
label2 = tk.Label(root, text="Hello2", bg="lightgreen")
label3 = tk.Label(root, text="Hello3", bg="lightblue")

label1.pack(side=tk.RIGHT)
label2.pack(side=tk.RIGHT)
label3.pack(side=tk.RIGHT)

root.mainloop()
