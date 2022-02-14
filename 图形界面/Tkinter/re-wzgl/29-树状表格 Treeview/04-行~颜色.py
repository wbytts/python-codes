"""
tag_configure("tag_name", options)

background：标签背景颜色
font：字形设置
foreground：标签前景色
image：图像与列表同时显示

将标签导入栏位：insert(..., tags="tag_name")
"""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

state_city = {
    "伊利诺": "芝加哥",
    "加州": "洛杉矶",
    "德州": "休斯顿",
    "华盛顿州": "西雅图",
    "江苏": "南京",
    "山东": "青岛",
    "广东": "广州",
    "福建": "厦门"
}

tree = ttk.Treeview(root, columns=("cities"))
tree.heading("#0", text="State")
tree.heading("#1", text="City")
tree.column("cities", anchor=tk.CENTER)
tree.tag_configure("even_color", background="lightblue")

row_count = 1
for state, city in state_city.items():
    if row_count % 2 == 1:
        tree.insert("", index=tk.END, text=state, values=city)
    else:
        tree.insert("", index=tk.END, text=state, values=city, tags=("even_color"))
    row_count += 1

tree.pack()

root.mainloop()
