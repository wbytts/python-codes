import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('400x200+0+0')

my_title = "一个人的旅行"
my_content = "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦" * 20

lab1 = tk.Label(root, text=my_title)
lab1.pack(padx=10, pady=10)

sep = ttk.Separator(root, orient=tk.HORIZONTAL)
sep.pack(fill=tk.X, padx=5)

lab2 = tk.Label(root, text=my_content)
lab2.pack(padx=10, pady=10)

root.mainloop()
