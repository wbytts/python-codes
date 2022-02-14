import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('800x600+0+0')

label = tk.Label(root)
label.pack()

label.config(text="0",
             fg="red", bg="skyblue",
             width=20, height=10,
             font="Helvetic 40 bold"
             )

count = 0


def start(lab):
    def count_num():
        global count
        count += 1
        label.config(text=str(count))
        label.after(1000, count_num)

    count_num()


start(label)

root.mainloop()
