
class A:
    __slots__ = ['a', 'b']


a = A()
a.a = 3
a.b = 4
#a.c = 5  # 这句话会报错

