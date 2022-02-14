import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# fill=NONE 默认值，保持原本大小
# fill=X 填满所分配的X轴，不留白
# fill=Y 填满所分配的Y轴，不留白
# fill=BOTH X轴和Y轴都填满

# 注意：如果所分配的容器已经填满了，那么fill参数将不会有作用

label = tk.Label(root, text="Hello World", bg="lightgreen")
label.pack(fill=tk.BOTH)

root.mainloop()
