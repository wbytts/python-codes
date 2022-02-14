

# 直接索引访问：D[key]
#如果访问字典中不存在的键，将导致 KeyError 出错信息
D = {'name': 'wby', 'age': 20}
print(D['name'])
# print(D['age']) # 这个会报错

# setdefault(key, default_value)：返回指定key对应的value，如果不存在则返回设置的默认值
print(D.setdefault('age', 24))
print(D.setdefault('sex', '男'))

# D.get(key) 如果存在这个键，则返回其值，如果不存在，则返回None
