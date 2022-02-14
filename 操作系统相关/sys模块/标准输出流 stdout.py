import sys

# 用法类似一个文件对象
sys.stdout.write('Hello, World\n')


# 手动重定向输出流

# 为了防止标准输出流引用丢失，可以用一个变量临时存储引用
temp = sys.stdout

sys.stdout = open('log.txt', 'a')
print('Hello World')

# 还原标准输出流
sys.stdout = temp
