# 将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
from collections import defaultdict
values = [11, 22, 33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)

for value in  values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
