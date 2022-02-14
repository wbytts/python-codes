# 对象的文档字符串，可以通过属性 __doc__ 查看

def hello():
    """
    这是文档字符串！！！！！
    :return:
    """
    pass


print(hello.__doc__)

# 内置的对象、方法、类、模块 等也会有文档字符串
print(open.__doc__)
