"""
column(id, options)
    id：指出特定栏位，名称字符串或者是 #x 的索引方式
    options：
        anchor：设置栏内容参考位置
        minwidth：最小栏宽，默认是20像素
        stretch：默认是1.当控件大小改变时，栏宽随着改变
        width：默认的栏宽是200像素

如果使用 column(id)，不传 options 参数，则返回指定栏的所有参数的内容

"""
