import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()
root.geometry('300x100+0+0')

pb = ttk.Progressbar(root, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=10, pady=10)
pb["maximum"] = 100
pb["value"] = 0


def running():
    while pb.cget("value") <= pb["maximum"]:
        pb.step(2)
        root.update()
        print(pb.cget("value"))
        time.sleep(0.05)


btn = tk.Button(root, text="开始", command=running)
btn.pack(pady=10)

root.mainloop()
