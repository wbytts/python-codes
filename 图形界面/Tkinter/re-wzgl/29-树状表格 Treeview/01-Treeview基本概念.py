"""
常用参数：
    columns：栏位的字符串，第一个栏位是图标栏（默认），不在此设置范围
    displaycolumns：设置栏位的显示顺序
        1. #all 表示显示所有栏，同时按照建立的顺序显示
        2. 如果设置 columns=("xxx", "xxx", "xxx")，使用insert插入元素时需要依次插入元素
            同样如果使用 columns(2, 0)：则数字表示实际的索引
    height：控件每行的高度
    padding：内容与控件框的间距
                  左  上  右  下
             a：  a   a   a   a
            ab:   a   b   a   b
           abc:   a   c   b   c
          abcd:   a   b   c   d

    selectmode：鼠标选择项目的方式
        BROWSER：默认值，一次一项
        EXTENDED：一次可以选择多项
        NONE：无法用鼠标进行选择
    show：默认是显示图标栏，设置为 show="headings"，则不显示图标栏
    takefocus：默认是True，如果不想被访问可以设为 False
"""
