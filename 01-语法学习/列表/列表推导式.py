
"""
列表推导式写在方括号中（提醒你在创建列表这个事实）
并且由使用了同一个变量名的表达式和循环结构组成

列表推导创建了新的列表作为结果，但是能在任何可迭代对象上进行迭代

列表推导只不过是通过对可迭代对象中的每一项应用一个表达式来构建一个新的列表的方式！
"""

lst1 = [i for i in range(10)]
print(lst1)

