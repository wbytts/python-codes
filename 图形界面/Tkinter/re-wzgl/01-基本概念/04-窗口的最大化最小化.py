import tkinter as tk

root = tk.Tk()

# root.state('zoomed') # 最大化窗口
# root.iconify() # 最小化窗口

tk.Button(root, text='最大化', command=lambda : root.state('zoomed')).pack()
tk.Button(root, text='最小化', command=lambda : root.iconify()).pack()

root.mainloop()
