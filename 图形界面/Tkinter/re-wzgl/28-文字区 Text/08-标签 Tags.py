"""
Tags：指一个区域文字，我们可以为这个区域取一个名字，可以用这个名字代表这个区域

常用方法：
    tag_add(tag_name, start_index[, end_index] ...)：将指定索引之间的文字设为标签
    tag_config(tag_name, options, ...)：对标签执行特定的编辑或动作绑定
        1. background：背景颜色
        2. borderwidth：文字外围厚度，默认是0
        3. font：字形
        4. foreground：前景颜色
        5. justify：对齐方式，
        6. overstrike：删除线（True）
        7. underline：下划线（True）
        9. wrap：NONE、CHAR、WORD
        ......
    tag_delete(tag_name)：删除标签，同时移除相关的编辑和事件绑定
    tag_remove(tag[,start_index[,end_index]])：删除标签，但是不溢出相关的编辑和事件绑定

系统有一个内建标签 SEL，表示选取的区间
"""
