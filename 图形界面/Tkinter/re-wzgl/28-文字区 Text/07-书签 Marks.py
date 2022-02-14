"""
Marks 书签：书签是无法显示的，但是会在编辑系统内被记录
如果书签内容被删除，则此书签也将自动被删除

默认有两个书签：INSERT、CURRENT

书签的常用方法：
    index(mark)：返回指定书签的 line 和 column
    mark_names()：返回Text对象的所有书签
    mark_set(mark, index)：在指定的index位置设置书签
    mark_unset(mark)：取消指定书签的设置
"""
