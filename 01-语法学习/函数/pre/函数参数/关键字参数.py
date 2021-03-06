
def fun(a, b, c, d, e):
    print(a, b, c, d, e)

# 位置传参调用
fun(1, 2, 3, 4, 5)
# 调用时可以直接指定参数名
fun(a=1, b=2, c=3, d=4, e=5)
# 当这么使用的时候，顺序可以是乱的
fun(b=2, d=4, a=1, e=5, c=3)
# 位置传参 和 关键字传参可以混合使用
fun(1, 2, 3, e=5, d=4)
# 但是要注意，位置参数要在关键字参数之前，下面的写法就是错的
# fun(e=5, d=4, 1, 2, 3)

# 使用列表解包方式传参
params = [1, 2, 3, 4, 5]
fun(*params)
# 使用字典解包方式传参
dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
}
fun(**dic)
# 当然，位置，关键字，序列解包，字典解包 等等 都是可以混用的
