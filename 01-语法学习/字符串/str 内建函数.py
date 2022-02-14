"""
str 表示字符串类型
"""

print(type(str))

"""
str 常用于其他类型转化为字符串类型
如 数字类型与字符串类型不能直接拼接，这时就可以把数字类型转为字符串类型
"""

a = 3
print('a = ' + str(a))

'''
大小写转换
'''
s = 'hello world'
# s.title() 每个单词首字母大写
print(s.title())
# s.lower() 所有字母小写
print(s.lower())
# s.upper() 所有字母大写
print(s.upper())


