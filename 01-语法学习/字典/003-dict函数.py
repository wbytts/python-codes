
# dict 函数创建一个空字典
D = dict()
print(D)

# dict.fromkeys(一个键的列表)，创建一个字典，默认有指定的一些键，它们的默认值是 None
D = dict.fromkeys(['a', 'b', 'c'])
print(D)
# 指定统一的默认值
D = dict.fromkeys(['a', 'b', 'c'], 666)
print(D)
# 使用元组指定默认值，不行，和上面一样的！
D = dict.fromkeys(['a', 'b', 'c'], (1, 2, 3))
print(D)
# 指定多个值呢？会报错
# D = dict.fromkeys(['a', 'b', 'c'], 1, 2, 3)
# print(D)
