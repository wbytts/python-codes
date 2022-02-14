import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# 可以用 padx 和 pady 来增加单元格之间的距离

tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=2, column=1, padx=10, pady=10)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=3, column=0, padx=10, pady=10)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=3, column=1, padx=10, pady=10)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=0, column=2, padx=10, pady=10)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=0, column=3, padx=10, pady=10)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=1, column=2, padx=10, pady=10)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=1, column=3, padx=10, pady=10)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=2, column=2, padx=10, pady=10)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=2, column=3, padx=10, pady=10)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=3, column=2, padx=10, pady=10)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=3, column=3, padx=10, pady=10)

root.mainloop()
