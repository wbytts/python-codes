"""
tkinter的Messagebox模块，提供了8个对话框

showinfo(title, message, options)：显示一半提示消息
showwarning(title, message, options)：显示警告消息
showerror(title, message, options)：显示错误消息
askquestion(title, message, options)：显示询问消息，单击是返回 yes，单击否返回 no
askokcancel(title, message, options)：显示确定或取消消息，单击是返回 True, 单击否返回 False
askyesno(title, message, options)：显示“是或否”，单击是返回 True，单击否返回 False
askyesnocancel(title, message, options)：显示“是或否或取消”，单击是返回 True，单击否返回 False，单击取消返回 None
askretrycancel(title, message, options)：显示“重试或取消”，单击重试返回 True，单击取消返回 False

options参数：
    default constant：默认按钮时 OK(确定)、Yes(是)、Retry(重试)在前面，可以更改
    icon(constant)：可以设定显示的图标，可选 INFO、ERROR、QUESTION、WARNING
    parent(widget)：支出当对话框关闭时，焦点窗口将返回给谁


注意导入语法：
    from tkinter imoprt messagebox

"""
