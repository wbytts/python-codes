import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

tk.Label(root, text="0行, 0列", width=30, height=5, bg="lightyellow").grid(row=0, column=0)
tk.Label(root, text="0行, 1列", width=30, height=5, bg="lightgreen").grid(row=0, column=1)
tk.Label(root, text="1行, 0列", width=30, height=5, bg="gray").grid(row=1, column=0)
tk.Label(root, text="1行, 1列", width=30, height=5, bg="skyblue").grid(row=1, column=1)

root.mainloop()
