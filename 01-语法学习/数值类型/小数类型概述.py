
# 小数 Decimal
# 从功能上讲，小数对象很像浮点数，但它们有固定的位数和小数点。因此小数的精度的固定的！
# 浮点数运算缺乏精确性，因为用来存储浮点数的空间有限

from decimal import Decimal


# Decimal 接收一个表示小数的字符串来构造小数对象
r = Decimal('0.1') + Decimal('0.2') + Decimal('0.3')
print(r)

# 当在表达式中混合使用不同精度的小数时，python会自动转换为最高的小数位数

# 设置全局小数精度
import decimal
decimal.getcontext().prec = 4

# 小数上下文管理器
# 可以使用 with 来临时重置小数精度，在with语句退出后，精度又被重置为初始值
with decimal.localcontext() as ctx:
    ctx.prec = 2
    r = Decimal(1) / Decimal('3')
    print(r)
