templist = [5, 6, 1, 2, 1, 0, 0, 5, 5, 3]
print(templist) # 原始列表

count = 0 # 记录列表中0元素的个数
while 0 in templist:
    templist.remove(0)
    count += 1 
print(templist) # 去除列表中的0元素

for i in range(count):
    templist.insert(0, 0)
print(templist) # 把对应0元素移动到列表起始位置
