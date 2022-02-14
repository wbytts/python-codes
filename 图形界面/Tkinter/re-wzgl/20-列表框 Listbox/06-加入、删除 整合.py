import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()


def item_add():
    var_add = entry.get()
    if len(var_add.strip()) == 0:
        return
    lb.insert(tk.END, var_add)
    entry.delete(0, tk.END)


def item_delete():
    index = lb.curselection()
    if len(index) == 0:
        return
    lb.delete(index)


entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_add = tk.Button(root, text="增加", width=10, command=item_add)
btn_add.grid(row=0, column=1, padx=5, pady=5)

lb = tk.Listbox(root)
lb.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

btn_del = tk.Button(root, text="删除", width=10, command=item_delete)
btn_del.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

root.mainloop()
