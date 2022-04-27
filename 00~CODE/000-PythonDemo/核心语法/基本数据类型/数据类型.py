
"""
为什么要区分数据类型：
    1. 要区分存储空间，不同数据占据的存储空间的大小和存储格式不一样

基本数据类型有：
* 数字类型
* 字符串类型
* 布尔类型

数字类型：整数、浮点数、复数。。。。。

字符串类型：使用单引号、双引号、三引号（三个单引号或者三个双引号）包裹起来
区别：
* 单引号和双引号没有区别
* 三引号包含的字符串可以进行换行书写

布尔类型表示真或者假，只有两个值 True(真)、False(假)

浮点型的表示：
123.432
.6
4.
"""

# 查看数据的类型
print(type(123))
print(type(3.14))
print(type(3+4j))
print(type("asd"))
print(type(True))

a = 1
print(type(a))  # <class 'int'> -- 整型

b = 1.1
print(type(b))  # <class 'float'> -- 浮点型

c = True
print(type(c))  # <class 'bool'> -- 布尔型

d = '12345'
print(type(d))  # <class 'str'> -- 字符串

e = [10, 20, 30]
print(type(e))  # <class 'list'> -- 列表

f = (10, 20, 30)
print(type(f))  # <class 'tuple'> -- 元组

h = {10, 20, 30}
print(type(h))  # <class 'set'> -- 集合

g = {'name': 'TOM', 'age': 20}
print(type(g))  # <class 'dict'> -- 字典