
class Person:

    # 在类体里面直接弄一个变量，就是给类增加了一个类属性
    name = 'person'

    def __init__(self):
        print("Person的 __init__ 方法执行了")



# 调用类对象，可以生成一个类实例对象，同时会执行类中的 __init__ 方法
p = Person()
# 测试对象能不能访问到 Person 的 name 属性
print(p.name)
# 给 p 赋值一个 name 属性
p.name = 'wby'
print(p.name)
print(Person.name)  # 给对象赋值name属性并不会覆盖Person的name属性

"""
看一下 p 有哪些属性：
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
"""
print(dir(p))
"""
看一下Person的属性，发现和p一样
"""
print(dir(Person))

# 对象有一个 __class__ 属性
print(p.__class__)  # <class '__main__.Person'> 打印出了这个对象对应的类型
print(Person.__class__)  # <class 'type'> 类型？是Person的类型是类型吗？

# p 可以通过 __class__ 属性找到 Person
# 访问p里面的属性时，如果p没有这个属性，就会通过 __class__ 找到类，然后去找类的属性

