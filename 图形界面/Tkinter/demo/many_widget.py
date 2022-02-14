import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext
import tkinter.tix as tix
import time


def progressbar():
    for i in range(100):
        progressbar1['value'] = i
        root.update()
        time.sleep(0.05)
    progressbar2.start()

def toplevel():
    top = tk.Toplevel()

def paint(event):
    x1, y1 = (event.x, event.y)
    x2, y2 = (event.x, event.y)
    canvas.create_rectangle(x1, y1, x2, y2, fill='red')

def show_popupmenu(event):
  popupmenu.post(event.x_root, event.y_root)

root = tix.Tk()
root.geometry('400x600+100+100')

menubar = tk.Menu()
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='打开'), filemenu.add_command(label='新 建'), filemenu.add_command(label='保存')
root.config(menu=menubar)

pw = tk.PanedWindow(root, orient='vertical', sashrelief='sunken')
pw.pack(fill='both', expand=1)
separator = ttk.Separator(root).pack(padx=2, fill='x')
status_frame = ttk.Frame(root, relief='raised').pack(fill='x')
label_status = ttk.Label(status_frame, text='状态栏').pack(side='left', fill='x')
sizegrip = ttk.Sizegrip(status_frame).pack(anchor='ne')

pw_1 = tk.PanedWindow(root, orient='horizontal', sashrelief='sunken')
pw_2 = tk.PanedWindow(root, orient='horizontal', sashrelief='sunken')
left_frame, right_frame, bottom_frame = ttk.Frame(pw_1, width=700,relief='raised'),\
ttk.Frame(pw_1, height=600, relief='raised'),\
ttk.Frame(pw_2, relief='raised')

pw.add(pw_1), pw.add(pw_2), pw_1.add(left_frame), pw_1.add(right_frame), pw_2.add(bottom_frame)

button, label, entry, radiobutton, checkbutton = ttk.Button(left_frame, text='按 钮',command=progressbar),\
ttk.Label(left_frame, text='标签'),\
ttk.Entry(left_frame),\
ttk.Radiobutton(left_frame,text='选项按钮'),\
ttk.Checkbutton(left_frame, text='复选框')

scale, labeledscale, spinbox = ttk.Scale(left_frame, from_=0, to=10, length=200,orient='horizontal'),\
ttk.LabeledScale(left_frame,from_=0,to=10), \
ttk.Spinbox(left_frame, from_=0, to=20, increment=2)

labelframe = ttk.LabelFrame(left_frame, text='标签框架')
scrollbar = ttk.Scrollbar(labelframe)
listbox = tk.Listbox(labelframe, height=6, width=5, yscrollcommand=scrollbar.set)
for i in range(20):
  listbox.insert('end', i)
scrollbar.config(command=listbox.yview)

stringvar1, stringvar2 = tk.StringVar(), tk.StringVar()
optionmenu = ttk.OptionMenu(left_frame, stringvar1, 'Python', 'Python', 'Java', 'Matlab')
combobox = ttk.Combobox(left_frame, textvariable=stringvar2, values=('Python', 'Java', 'Matlab'))

progressbar1, progressbar2 = ttk.Progressbar(left_frame, orient='horizontal', value=0, length=200,mode='determinate'),\
ttk.Progressbar(left_frame,orient='horizontal',value=0,length=200,mode='indeterminate')

button.pack(pady=2), label.pack(pady=2), entry.pack(pady=2), radiobutton.pack(pady=2), checkbutton.pack(pady=2),\
scale.pack(pady=2), labeledscale.pack(), spinbox.pack(),
labelframe.pack(), scrollbar.pack(side='right', fill='y'), listbox.pack(side='left',fill='y'), \
optionmenu.pack(), combobox.pack(), progressbar1.pack(), progressbar2.pack()

menubutton = ttk.Menubutton(right_frame, text='单选按钮')
menubutton.pack()
mb_menu = tk.Menu(menubutton, tearoff=0)
mb_menu.add_radiobutton(label='选项按钮'), mb_menu.add_command(label='命令按钮'),\
mb_menu.add_checkbutton(label='复选按钮'), mb_menu.add_separator(), mb_menu.add_command(label='退出', command=root.destroy)
menubutton.config(menu=mb_menu)

button_top = ttk.Button(right_frame, text='顶层窗口', command=toplevel)
button_top.pack()

treeview_sheet = ttk.Treeview(right_frame, height=10, columns=('图标 栏'), selectmode='extended')
treeview_sheet.heading('#0', text='图标栏1'), treeview_sheet.heading('#1', text='图标栏2')
for i in range(30):
  treeview_sheet.insert('', index='end', text=i, values=i)
treeview_tree = ttk.Treeview(right_frame, height=10, show='tree')
treeview_tree_parents = treeview_tree.insert('', index='end', text='结构树')
for i in range(10):
  treeview_tree.insert(treeview_tree_parents, index='end', text=i)

frame_nb1, frame_nb2 = ttk.Frame(right_frame), ttk.Frame(right_frame)
notebook = ttk.Notebook(right_frame, height=200, width=200)
notebook.add(frame_nb1, text='选项卡1'), notebook.add(frame_nb2, text='选项卡2')

canvas = tk.Canvas(right_frame, bg='white', height=300, width=300)
canvas.create_line(10, 10, 50, 30, 60, 70)
canvas.bind('<B1-Motion>', paint)

text = tkinter.scrolledtext.ScrolledText(bottom_frame, height=5).pack(side='left', fill='both', expand=1)

balloon = tix.Balloon(right_frame)
balloon.bind_widget(button_top, balloonmsg='这是一个气泡提示')

popupmenu = tk.Menu(root, tearoff=0)
popupmenu.add_command(label='最小化', command=root.iconify),\
popupmenu.add_command(label='退出', command=root.destroy)
root.bind('<Button-3>', show_popupmenu)

treeview_sheet.pack(side='left', padx=5), treeview_tree.pack(side='left', padx=5),notebook.pack(side='left',padx=5),\
canvas.pack(side='left', padx=5)

root.mainloop()

