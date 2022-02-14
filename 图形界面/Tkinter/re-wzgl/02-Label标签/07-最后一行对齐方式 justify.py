import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# justify 设置多行文字时，最后一行的对齐方式
# 可以取值为，left居左，center居中，right居右 （默认是居中）
label = tk.Label(root, text="aasbdajsdjksafjkdsfbdskjfjsdgbkjfsgbkjdfsnfkjsfnkjnwjkadnfkjadnkfjnsdkjfndskjfd",
                 fg="red", bg="skyblue",
                 width=20, height=20,
                 wraplength=120,
                 justify="right")
label.pack()

root.mainloop()
