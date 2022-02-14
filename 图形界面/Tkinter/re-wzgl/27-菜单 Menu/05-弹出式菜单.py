import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

pop_menu = tk.Menu(root, tearoff=False)
pop_menu.add_command(label="菜单项1", command=lambda: print("菜单项1点击了"))
pop_menu.add_command(label="菜单项2", command=lambda: print("菜单项2点击了"))

root.bind("<Button-3>", lambda e: pop_menu.post(e.x_root, e.y_root))

root.mainloop()
