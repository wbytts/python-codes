

s = 'hello world'
print(s[::-1])

# 字符串中好像没有 reverse 方法？

# 内置函数 reversed，能翻转，但是返回的是 <reversed object at 0x0000000001215C10> 这种
s = reversed(s)
print(s)
# 可以用 list 转换为列表
s = list(s)
print(s)
# 然后把字典拼接为字符串
s = ''.join(s)
print(s)

