import sys

# print 用来输出数据

# 输出一个字符串
print("Hello World")

# 输出多个数据
print("a", 1, 3.14)

# 默认print以空格分割多个值，可以通过 sep 指定
print(1,2,3,sep="$$$")

# 默认print以换行符结尾，可以通过end指定
print("aaaaa")
print("bbbbbbbbbb")
print("cccccc", end="#")
print("ddddddddddd")

# file 指定输出对象
print("aaa", file=sys.stdout) # 这是默认的，file可以换成文件等其他

"""
flush 选项及输出缓冲区的概念
"""

name = 'asd'
age = 100
s = 'my name is %s my age is %d' % (name, age)
print(s)

print('#%-6d#' % -12)

print('1111111111', '123123123123')

# help(print)

"""
Python2中 print是一个语句，而不是一个函数
"""


print('\tpython')
print('\npython')
print('\ntpython')
