import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('300x200+0+0')

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="退出", command=root.destroy)
view_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="视图", menu=view_menu)


def change_status():
    if demo_status_var.get():
        status_lab.pack(side=tk.BOTTOM, fill=tk.X)
    else:
        status_lab.pack_forget()


demo_status_var = tk.BooleanVar()
demo_status_var.set(True)
view_menu.add_checkbutton(label="状态", variable=demo_status_var, command=change_status)
root.config(menu=menubar)

status_lab_var = tk.StringVar()
status_lab_var.set("显示")
status_lab = tk.Label(root, textvariable=status_lab_var, relief="raised")
status_lab.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
