
'''
下面这几个方法返回可迭代对象：
    D.keys()：收集字典中的所有键
    D.values()：收集字典中的所有值
    D.items()：收集字典中的所有键值对  元素是(key, value) 组成的元组
'''

D = {'name': 'wby', 'age': 20}
print(D.keys())
print(D.values())
print(D.items())

print('-' * 50)
# 它们返回的并不是列表类型，我们可以将他们转换为列表类型
print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))
