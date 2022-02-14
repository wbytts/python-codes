import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)

left_frame = tk.LabelFrame(pw, text="Left", width=120, height=150)
pw.add(left_frame)

middle_frame = tk.LabelFrame(pw, text="Middle", width=120)
pw.add(middle_frame)

right_frame = tk.LabelFrame(pw, text="Right", width=120)
pw.add(right_frame)

pw.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
