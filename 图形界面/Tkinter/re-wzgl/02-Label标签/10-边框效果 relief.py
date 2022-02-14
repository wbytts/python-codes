import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')


# borderWidth 控制边框宽度

# relief 可选的值有
# flat
# groove
# raised
# ridge
# solid
# sunken
label = tk.Label(root, text="Hello World", relief="raised", borderwidth=5)
label.pack()

root.mainloop()
