# 分数、有理数：Fraction
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y) # 会自动化简为最简分数
print(x + y)

# 分数转换
# 浮点数对象提供了一个方法，能够产生它们的分子和分母比  f.as_integer_ratio()
# 分数有一个from_float方法，并且float函数可以接收一个Fraction对象作为参数
print(1.5.as_integer_ratio()) # 一个元组：(分子, 分母)

# 用一个浮点数创建一个分数
frac = Fraction(*3.14.as_integer_ratio())
print(frac)
# 尽管可以从浮点数转换为分数，但是浮点数本身就是不精确的，即使转换为分数也是会保留最初的精度损失
# 有时候，我们可以限制分母的最大值来简化这样的结果
frac = Fraction(*3.14.as_integer_ratio())
print(frac)
frac = frac.limit_denominator(10)  # 并不会修改原分数，而是返回一个新的对象
print(frac)


