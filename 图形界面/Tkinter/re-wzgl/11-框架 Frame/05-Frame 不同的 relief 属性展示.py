import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

"""
# flat
# groove
# raised
# ridge
# solid
# sunken
"""

reliefs = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']

index = 0
for i in range(0, 3):
    for j in range(0, 2):
        frm = tk.Frame(root, width=400, height=80, relief=reliefs[index], borderwidth=1)
        frm.grid(row=i, column=j, padx=5, pady=5)
        index += 1


root.mainloop()
