import tkinter as tk
import tkinter.ttk as ttk
import my_handlers as mh
import os

root = tk.Tk()
root.geometry('900x600+0+0')
root.title('WIN工具箱 by 冰冰')

fun_dict = {
    "控制台": lambda _: os.system("start"),
    "计算器": lambda _: os.system("start calc"),
    "记事本": lambda _: os.system("start notepad"),
    "控制面板": lambda _: os.system("start control"),
    "注册表": lambda _: os.system("start regedit"),
    "服务": lambda _: os.system("start services.msc"),
    "Windows版本": lambda _: os.system("start winver"),
    "资源管理器": lambda _: os.system("start explorer"),
    "画图": lambda _: os.system("start mspaint"),
}

btns = []
for r in range(0, 10):
    for c in range(0, 10):
        btn = tk.Button(root, text=f'{r}-{c}', width=10, height=2)
        btn.grid(row=r, column=c, padx=5, pady=5)
        btns.append(btn)

index = 0
for text, func in fun_dict.items():
    btns[index]["text"] = text
    btns[index].bind("<Button-1>", func)
    index += 1

root.mainloop()
