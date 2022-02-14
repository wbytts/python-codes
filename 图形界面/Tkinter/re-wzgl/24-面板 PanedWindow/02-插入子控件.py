import tkinter as tk

pw = tk.PanedWindow(orient=tk.VERTICAL)
pw.pack(fill=tk.BOTH, expand=True)

top = tk.Label(pw, text="Top")
# ttk 模块中的 PanedWindow 的 add 方法还可以设置 weight，表示各个组件的比重
pw.add(top)

bottom = tk.Label(pw, text="Bottom")
pw.add(bottom)

pw.mainloop()
