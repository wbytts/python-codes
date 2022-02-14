'''
datetime包是Python处理日期和时间的标准库
'''
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
from datetime import datetime, timedelta, timezone

# 获取当前的日期和时间
now = datetime.now()
print(now)

# 获取指定的日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 转化为时间抽
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
# 可以认为：timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# python这个包里的时间戳是 秒 为单位
print(dt.timestamp())

# 时间戳转化为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
# UTC时间
print(datetime.utcfromtimestamp(t))

# str 转换为 datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转换为 str
print(dt.strftime('%a, %b %d %H:%M'))

# datetime加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


# 时区转换
'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
'''
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

'''
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''
