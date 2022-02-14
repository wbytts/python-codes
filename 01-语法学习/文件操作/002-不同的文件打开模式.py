
# w是写入，r是读取，a是追加，b是二进制文件。具体还要看C里，应该和它一样
f = open('a.txt', 'w', encoding='utf8')
f.write("你好啊")
f.close()
