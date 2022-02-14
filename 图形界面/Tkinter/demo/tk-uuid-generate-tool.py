import tkinter as tk
from tkinter import ttk
import uuid
import pyperclip


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('UUID生成工具 ~ by wangby')
        self.root.geometry('280x140+200+200')
        self.root.resizable(False, False)
        self.init_widget()
        self.bind_event()

    def init_widget(self):
        self.var_title = tk.StringVar()
        self.lab_title = tk.Label(self.root, textvariable=self.var_title)
        self.lab_et_prefix = tk.Label(self.root, text='前缀')
        self.id_prefix = tk.StringVar()
        self.et_prefix = tk.Entry(self.root, textvariable=self.id_prefix)
        self.btn_generate = tk.Button(self.root, text='生成UUID')
        self.btn_copy = tk.Button(self.root, text='拷贝')
        self.pack_widget()

    def pack_widget(self):
        self.lab_title.place(x=10, y=10)
        self.lab_et_prefix.place(x=20, y=40)
        self.et_prefix.place(x=60, y=40)
        self.btn_generate.place(x=20, y=80)
        self.btn_copy.place(x=120, y=80)

    def bind_event(self):
        self.btn_generate.bind('<Button-1>', self.generate_uuid)
        self.btn_copy.bind('<Button-1>', self.copy_uuid)

    def generate_uuid(self, event):
        id = uuid.uuid4().hex
        prefix = self.id_prefix.get()
        self.var_title.set(prefix + id)

    def copy_uuid(self, event):
        pyperclip.copy(self.var_title.get())

    def run(self):
        self.root.mainloop()


app = App()
app.run()
