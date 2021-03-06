# 直接赋值
a = 3

# 连续赋值
x = y = z = 4


"""
复合赋值：
    一些操作符可以和赋值运算符组合，形成新的运算符：
        如： +=， A += B，相当于 A = A + B
        其他类似的有：
            -=
            *=
            /=
            **=
            等等
"""


"""
解包赋值：（unpack）
    a, b, c, ... = 序列
        将序列的值拆成多个名字，左侧的名字个数需要和序列的长度相同
    a, b, c, *s = 序列
    a, b, *s, c = 序列
    *s, a, b, c = 序列
        加上星号，可以将序列中剩下的内容收集起来，作为一个列表
"""

lst = [5, 4, 3, 2, 1]

a, b, c, d, e = lst
print(a, b, c, d, e)

a, b, c, *s = lst
print(a, b, c, s)

a, b, *s, c = lst
print(a, b, s, c)
