import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# 注：如果要用上下箭头改变数值，必须将插入点放在数值区里
spin = tk.Spinbox(root, from_=10, to=30, increment=2)
spin.pack(pady=20)

# 可以用 get 方法取得当前的值
print(spin.get())

root.mainloop()
