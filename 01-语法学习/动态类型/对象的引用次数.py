import sys

# 查看3这个对象被引用了多少次
print(sys.getrefcount(3)) # 可以看到，默认情况下，在py解释器中，3已经被引用了很多次了

a = 3
b = 3

print(sys.getrefcount(3)) # 这里，3的引用次数增加了2次


