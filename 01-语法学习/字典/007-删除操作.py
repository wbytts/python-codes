
D = {'name': 'wby', 'age': 20}
print(D)
# 删除字典中的一个键
del D['name']
print(D)
# 删除整个字典
del D
# print(D) # 这个会报错，因为 del D 之后，变量D就没有引用对象了

print('-' * 50)
D = {'name': 'wby', 'age': 20}
# D.pop(key) 获取指定键的值，并删除这个键
value = D.pop('name')
print(D)
print(value)

print('-' * 50)
# D.popitem() 随机弹出一个键值对，以元组的形式返回 (键, 值)
D = {'name': 'wby', 'age': 20}
result = D.popitem()
print(D)
print(result)

print('-' * 50)
D = {'name': 'wby', 'age': 20}
# D.clear() 清空字典
D.clear()
print(D)
