a = [1, 2, 3, 4, 5, 6, 7, 8]

# del 删除变量的关键字，可用于删除列表的数据
del a[2]
print(a)
# pop() 删除末尾元素
x = a.pop()
print(a, x)
# pop(i) pop可以写一个参数，可以弹出指定索引的元素
x = a.pop(1)
print(a, x)

# remove(obj) 删除指定的值
a.remove(1)
print(a)

# clear() 清空列表
a.clear()
print(a)
