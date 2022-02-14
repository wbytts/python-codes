import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

# wraplength ，文字在多少宽度之后换行
# 注意，这个单位是像素，而不是换行哦！（和宽高不一样了）
label = tk.Label(root, text="aasbdajsdjksafjkdsfbdskjfjsdgbkjfsgbkjdfsnfkjsfnkjnwjkadnfkjadnkfjnsdkjfndskjfd",
                 fg="red", bg="skyblue",
                 width=20, height=20,
                 wraplength=50)
label.pack()

root.mainloop()
