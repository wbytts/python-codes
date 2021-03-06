
# X / Y：经典除法 和 真除法
# 在python2.x 这个操作对于整数会省去小数部分，对于浮点数会保持余项（小数部分）
# 在python3中，这个操作是真除法，最终是浮点数结果，且会保留小数部分

# X // Y：向下取整除法
# python2.2新增的操作，不考虑对象的类型，总是省略结果的小数部分，剩下最小的能整除的整数部分
# 结果的类型取决于操作数的类型

# 使用一个从 __future__ 模块的导入，可以在python2.x中开启python3.x的 / 真除法，而不是用float转换来强制它
