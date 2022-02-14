from collections import namedtuple

'''
一个 tuple (1, 2) 表示坐标
但是直接看，并不会确定认为它是坐标
定义一个class又小题大做了，这时，namedtuple就派上了用场
'''

Point =namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
Point对象是tuple的一种子类
'''
