def f(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l

# 再次调用函数
print(f(1))
print(f(2))
print(f(3))

# 返回值
# [1]
# [2]
# [3]
