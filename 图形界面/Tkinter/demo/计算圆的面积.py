import tkinter as tk
import math

app = tk.Tk()

tk.Label(app, text="圆的半径").grid(row=0, column=0)
e_raduis = tk.Entry(app)
e_raduis.grid(row=0, column=1)

btn_calc = tk.Button(app, text="计算圆的面积")
btn_calc.grid(row=1, column=0, columnspan=2)


tk.Label(app, text="面积").grid(row=2, column=0)
lab_result = tk.Label(app)
lab_result.grid(row=2, column=1)


def calc_area(event):
    r_str = e_raduis.get()
    r = int(r_str)
    lab_result.configure(text=str(r * r * math.pi))


btn_calc.bind('<Button-1>', calc_area)

app.mainloop()
