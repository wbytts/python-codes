f = open('a.txt', 'w', encoding='utf8')
# 写入字符（不是写入一行）
f.write("你好啊")
f.write("我很好")

# 写入多行，相当于多次 write，也不会再末尾添加换行
lines = ["Hello", "World", "LA\n", "LA", "LA"]
f.writelines(lines)

# 判断文件是否可写入
print(f.writable())
# 判断文件是否可读取
print(f.readable())

f.close()
