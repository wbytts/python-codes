import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()

pb = ttk.Progressbar(root, length=200, mode="determinate", orient=tk.HORIZONTAL)
pb.pack(padx=5, pady=10)
pb["maximum"] = 100
pb["value"] = 0

btn_start = tk.Button(root, text="开始", command=pb.start)
btn_start.pack(side=tk.LEFT, padx=40, pady=10)

btn_stop = tk.Button(root, text="停止", command=pb.stop)
btn_stop.pack(side=tk.LEFT, padx=15, pady=10)

root.mainloop()
