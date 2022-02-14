
'''
浮点数在标准的CPython中采用C语言中的 “双精度” 来实现
其精度与用来构建Python解释器的C编译器所给定的双精度一样
'''

# is_integer 测试一个浮点数类型对象是否是一个整数（数学上）
a = 3.14
print(a.is_integer())
a = 3.0
print(a.is_integer())

# as_integer_ratio
