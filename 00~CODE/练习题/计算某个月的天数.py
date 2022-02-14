year = int(input("请输入年份:"))
month = int(input("请输入月份:"))

# 生成每个月的天数
# 一月大、二月小、三月大、四月小、五月大、六月小、七月大、八月大、九月小、十月大、十一月小、十二月大（数手指头得出来的）
month_days = {k: 31 if k in [1, 3, 5, 7, 8, 10, 12] else 30 for k in range(1, 12 + 1)}

# 判断是否是闰年（模400余0的是世纪闰年，模4余0的是普通闰年）
# 如果是闰年2月是29天，否则2月是28天，这里先默认2月是30天
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_days[2] = 29
else:
    month_days[2] = 28

# 查字典获得对应月份的天数
days = month_days[month]

print("%d年%d月的天数是: %d" % (year, month, days))
