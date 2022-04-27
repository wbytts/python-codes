# 带有默认值的字典
from collections import defaultdict
dic = defaultdict(list)    	# 定义字典值数据类型list
dic["key1"].append(12)		# 将值添加到列表中，键为key1
print(dic)   # {'key1': [12]}
