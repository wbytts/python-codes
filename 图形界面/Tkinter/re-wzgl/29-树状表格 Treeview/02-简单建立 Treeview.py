import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

tree = ttk.Treeview(root, columns=("Cities"))

# 建立标题栏
tree.heading("#0", text="State")
tree.heading("#1", text="City")

# 插入内容
# text：设置图标栏的内容
# values：设置一般栏位的内容
tree.insert("", index=tk.END, text="伊利诺", values="芝加哥")
tree.insert("", index=tk.END, text="加州", values="洛杉矶")
tree.insert("", index=tk.END, text="江苏", values="南京")
tree.pack()

root.mainloop()
