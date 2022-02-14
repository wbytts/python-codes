
# 已有键和值的列表(或可迭代对象)
keys = ['A', 'B', 'C', 'D', 'E']
values = [1, 2, 3, 4, 5]

# 使用 zip 构造字典
D = {}
for (k, v) in zip(keys, values): D[k] = v
print(D)
# 或者更简单的，使用字典推导式
D = {k: v for (k, v) in zip(keys, values)}
print(D)
# 或者使用 dict 函数
D = dict(zip(keys, values))
print(D)
