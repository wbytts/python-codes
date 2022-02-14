
'''
对一个字典中不存在的键赋值，那么会创建这个键（并不会报错）

D[key] = value，如果key存在，则修改，如果key不存在，则新增

也就是说，字典中的键，不会重复，是唯一的！
'''

D = {}
D['name'] = 'wby'
D['age'] = 20

print(D)

print('-' * 50)
# D.update(D2) 用另一个字典更新当前字典
D = {'name': 'wby', 'age': 20}
D2 = {'age': 24}
D.update(D2)
print(D)

