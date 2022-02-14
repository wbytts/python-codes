import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=0, column=0)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=0, column=1)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=1, column=0)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=1, column=1)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=2, column=0)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=2, column=1)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=3, column=0)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=3, column=1)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=0, column=2)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=0, column=3)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=1, column=2)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=1, column=3)
tk.Label(root, text="0行, 0列", width=20, height=3, bg="lightyellow").grid(row=2, column=2)
tk.Label(root, text="0行, 1列", width=20, height=3, bg="lightgreen").grid(row=2, column=3)
tk.Label(root, text="1行, 0列", width=20, height=3, bg="gray").grid(row=3, column=2)
tk.Label(root, text="1行, 1列", width=20, height=3, bg="skyblue").grid(row=3, column=3)

# row 0 的控件在窗口大小改变时，缩放比是1
root.rowconfigure(0, weight=1)
# column 0 的控件在窗口大小改变时，缩放比是1
root.columnconfigure(0, 1)

root.mainloop()
