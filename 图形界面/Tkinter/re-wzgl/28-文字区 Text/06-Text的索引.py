"""
Text对象的索引是一个字符串
    "line.column"：line从1开始，column从0开始，中间用点分隔
    INSERT：目前插入点的位置
    CURRENT：光标目前相对于字符的位置
    END：缓冲区最后一个字符的位置
    索引表达式：
        +count chars：count是数字，如 +2c 是索引向后移动两个字符
        -count chars：count是数字，如 -2c 是索引向前移动两个字符

也可以使用 index 方法，实际用字符串方式列出索引内容
"""
