import tkinter as tk

root = tk.Tk()
# 设置窗口的标题
root.title('标题')
# 设置窗口的宽高位置
root.geometry('200x200+200+200')
# 设置拖拽的最大宽高
root.maxsize(600, 600)
# 设置拖拽的最小宽高
root.minsize(100, 100)
# 设置窗口是否可以更改大小
root.resizable(True, True)

# 更改窗口默认图标
root.iconbitmap('xxx.ico')

# 等待，并处理窗口事件
root.mainloop()
