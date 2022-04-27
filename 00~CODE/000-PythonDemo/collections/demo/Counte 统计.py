from collections import Counter
s = [1,1,2,2,3,3]
print(dict(Counter(s)))  # {1: 2, 2: 2, 3: 2}

s1 = ("a",2,3,3,"a",2,"a",1,"a")
print(dict(Counter(s1))) # {'a': 4, 2: 2, 3: 2, 1: 1}
# 统计元素出现的次数,以字典的形式输出
