"""
Label方法可以用于在窗口内建立文字或图像标签
    Label(父对象, options...)

选项说明：
    anchor：如果控件大于所需时，控制标签的位置，默认是CENTER（居中）
    bg或background：背景色彩
    bitmap：使用默认图标当做标签内容
    bd或borderwidth：标签边界宽度，默认为1
    compound：可以设置标签内含图像和文字时，彼此的位置关系
    cursor：当鼠标光标在标签上方时的外形
    fg或foreground：前景色彩
    font：可选择字形、样式、大小
    height：标签高度，单位是字符
    image：标签以图像方式呈现
    justify：存在多行文本时，最后一行的对齐方式，可取值 ：LEFT、CENTER、RIGHT，默认是居中对齐
    padx/pady：标签文字与标签区间的间距，单位是像素
    relief：默认是relief=FLAT，可由此控制标签的外框
    text：标签内容，如果有 '\n' 可以输入多行文字
    textvariable：可以设置标签以变量的方式显示
    underline：可以设置第几个文字有下划线，从0开始算起，默认是-1，表示无下划线
    width：标签宽度，单位是字符
    wraplength：文本到多少宽度后换行，单位是像素
"""

from tkinter import *


root = Tk()
root.title('title')
label = Label(root, text='XXX')

# 注意 pack 方法，并不返回组件实例，而是 None
label.pack()

root.mainloop()
