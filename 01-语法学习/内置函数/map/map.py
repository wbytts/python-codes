
lis = [1, 2, 3, 4, 5]

"""
map(函数, 序列)
对序列的每个元素应用函数，函数的参数为序列的元素

更一般的：map把一个函数应用于传入的可迭代对象的每一项，返回一个新的可迭代对象（map对象）
注：这也是为什么map中函数是第一个参数！
"""
map_res = map(lambda x: x*x, lis)
print(type(map_res))
print(map_res)
print(list(map_res))

a_list = [1, 2, 3, 4, 5]

def 乘2(x):
    return x * 2

map_result = map(乘2, a_list)

new_list = list(map_result)

print(new_list)
