"""
pack在tkinter中是一个类别，提供了一些方法
    slaves()：返回所有widget控件对象
    info()：返回pack选项的对应值
    forget()：隐藏widget，可以用 pack(option...) 复原显示
    location(x,y) 判断此点是否存在单元格，如果是则传回坐标，如果不是返回 (-1, -1)
    size() 返回widget的大小
    propagate(boolean) 如果是True表示，父窗口大小由子控件决定，默认为 True

"""
