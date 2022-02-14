
'''
from collections import namedtuple
'''

from collections import namedtuple

# 创建一个有名元组
a = namedtuple('a', ['name', 'age', 'sex'])
print(a)
# 转换为一个类字典的基于键的形式 x._asdict()

# 有名元组是一个元组、类、字典的混合体
