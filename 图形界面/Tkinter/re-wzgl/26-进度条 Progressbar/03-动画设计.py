import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()
root.geometry('300x100+0+0')

pb = ttk.Progressbar(root, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=10, pady=10)
pb["maximum"] = 100
pb["value"] = 0


def start():
    for i in range(100):
        pb["value"] = i + 1
        root.update()
        time.sleep(0.05)


btn = tk.Button(root, text="开始", command=start)
btn.pack(pady=10)

root.mainloop()
