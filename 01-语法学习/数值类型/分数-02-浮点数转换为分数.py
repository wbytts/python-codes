from fractions import Fraction

# 尽管可以从浮点数转换为分数，但是浮点数本身就是不精确的，即使转换为分数也是会保留最初的精度损失
# 有时候，我们可以限制分母的最大值来简化这样的结果
frac = Fraction(*float("3.14").as_integer_ratio())
print(frac)

frac = frac.limit_denominator(100)  # 并不会修改原分数，而是返回一个新的对象
print(frac)
