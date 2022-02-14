a = "123"
b = "asd"
print(a+b)

# 如果没有逗号，python会在表达式中自动拼接吸纳桂林的字符串字面量
print("123" "asd")

a = "123"
b = ['a', 's', 'd']

# s.join(序列) 使用 s 来连接序列中的元素
# 通常用作列表转字符串
s = a + ''.join(b)
print(s)
