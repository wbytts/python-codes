import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('800x600+0+0')
img = Image.open("apple.jpg")
img_tk = ImageTk.PhotoImage(img)
label = tk.Label(root, image=img_tk)
label.pack()

root.mainloop()
