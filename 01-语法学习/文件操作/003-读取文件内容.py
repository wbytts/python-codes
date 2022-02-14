
f = open('a.txt', 'r', encoding='utf8')
# 读取所有内容
# s = f.read()

# 读取一行内容，默认包含换行
# s = f.readline()

# 读取所有行
s = f.readlines()
print(s)

# 判断文件是否可写入
print(f.writable())
# 判断文件是否可读取
print(f.readable())
f.close()
