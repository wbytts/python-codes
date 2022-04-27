# 生成可以使用名字来访问元素内容的tuple
# namedtuple('名称', [属性list])

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)   		# Point(x=1, y=2)
