import tkinter as tk
from tkinter import messagebox
from tabview import TabView

# 在body中生成widget的函数，返回的widget将被添加到tabview的body中
def create_body():
    global body
    return tk.Label(body, text="this is body")

# 点击选项卡时的回调
def select(index):
    print("current selected -->", index)

# 删除选项卡时的回调，如果返回False将不会删除
def remove(index):
    print("remove tab -->", index)
    if messagebox.askokcancel("标题", "确定要关闭该选项卡吗？"):
        return True
    else:
        return False

# ----------------------- 使用示例 ----------------------------
root = tk.Tk()
root.geometry("640x300")

tab_view = TabView(root, generate_body=create_body,
                   select_listen=select, remove_listen=remove)

body = tab_view.body

label_1 = tk.Label(tab_view.body, text="this is tab1")
label_2 = tk.Label(tab_view.body, text="this is tab2")

# 第一个参数是向body中添加的widget, 第二个参数是tab标题
tab_view.add_tab(label_1, "tabs1")
tab_view.add_tab(label_2, "tabs2")

# TabView需要向x、y方向填充，且expand应设置为yes
tab_view.pack(fill="both", expand='yes', pady=2)

root.mainloop()
