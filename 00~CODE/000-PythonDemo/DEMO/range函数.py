"""
range(x)：生成0到x的区间，不包括x
range(a, b)：生成a到b的区间，不包括b
range(a, b, k)：在a到b的区间中，每隔k个元素取一个
"""
for i in range(10):
    print(i, end=", ")
print()

for i in range(3, 8):
    print(i, end=", ")
print()

for i in range(3, 12, 2):
    print(i, end=", ")

print(range(10))
