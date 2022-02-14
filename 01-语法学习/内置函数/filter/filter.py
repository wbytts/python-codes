data = [1, 2, 3, 4, 5, 6, 7, 8]

# filter 过滤
# 第一个参数：一个函数，参数是当前的元素。返回值为True的话，就表示这个元素保留
# 第二个参数：操作的序列
# 返回值，满足条件的元素，类型 filter
res = list(filter(lambda x: x % 2 == 1, data))

print(res)
