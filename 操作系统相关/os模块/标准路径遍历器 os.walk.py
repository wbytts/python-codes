
'''
os.walk() 是一个简单的可迭代对象
'''

import os

res = os.walk('f:/images')
print(res)

for i in res:
    print(i)

