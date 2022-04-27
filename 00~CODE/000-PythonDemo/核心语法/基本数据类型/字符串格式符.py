"""
字符串格式符语法：
    %[(name)][flags][width][.precision]typecode

    (name)：表示根据指定的名称（key）来查找对应的值，格式化到字符串当中
    flags：表示对齐的方式（默认右对齐）
        空：右对齐
        -：左对齐
        空格：表示在整数左侧填充一个空格，从而与负数对齐
    width：表示占据的宽度
    .precision：表示小数点后的精度
    typeCode：

"""

a = 3
b = 4

print("a=%d, b=%d" % (a, b))
# 如果只有一个数据，也可以不用元组
print("a=%d" % a)
# 也可以使用字典来进行格式化赋值，不过要通过(name)指定对应的键值
print("a=%(a)d, b=%(b)d" % {"a": a, "b": b})
