
a = [1, 2, 3, 4, 5]

# L[:] 相当于创建了列表的一个拷贝
b = a[:]
print(b)

# 那么 L[:] 是深拷贝还是浅拷贝呢？
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
b[0][0] = 999
print(a)
print(b)
# 这个也是浅拷贝，即切片赋值形成的新列表
