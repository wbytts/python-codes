a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# 默认返回 zip py类型检查
print(zip(a, b))

# zip py类型检查
for x, y in zip(a, b):
    print(x, y)

for item in zip(a, b):
    print(item)

# 使用 list 可以转换成列表类型
print(list(zip(a, b)))

# zip 可以压缩多个列表，例如 zip(a, b, c)
# 如果zip压缩的列表长度不相等，最终的个数以短的为准
print(list(zip(
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4]
)))


