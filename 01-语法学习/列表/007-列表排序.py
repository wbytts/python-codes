
a = [1, 5, 2, 4, 3]

# L.sort() 方法会修改列表本身，默认是从小到大排序
# 可以指定 reverse 参数，从大到小排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 使用系统内置的 sorted 函数排序，默认是从小到大排序
# sorted 不会修改列表本身，而是返回排序后的一个新列表
a = [1, 5, 2, 4, 3]
a = sorted(a)
print(a)
a = sorted(a, reverse=True)
print(a)
# sorted 可以指定一个 reverse 参数，默认是False，如果是True表示从大到小排序


# 总结：用法上 L.sort() 和 sorted() 差不多，但是 sorted 不会改变原列表的顺序
