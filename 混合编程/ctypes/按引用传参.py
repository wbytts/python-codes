# 引入C的相关支持
from ctypes import *

# 加载C的核心动态链接库
# MS：Microsoft Visual C++ Runtime 微软VC运行时环境
msvcrt = cdll.msvcrt

# 创建一个C语言的int类型的（变量---此处是C的变量概念）
num = c_int()
print("输入一个整数:", end='')

# 调用C的scanf函数，获取输入
# byref(x) 按引用传参（按地址传参）相当于C里面的 &
msvcrt.scanf(b"%d", byref(num))

# 打印输入的值
print('输入的值:', num.value)


