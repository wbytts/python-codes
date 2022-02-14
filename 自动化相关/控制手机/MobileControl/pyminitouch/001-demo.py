from pyminitouch import MNTDevice

_DEVICE_ID = '192.168.1.4:5555'
device = MNTDevice(_DEVICE_ID)


# 单点触控
device.tap([(400, 600)])
# 多点触控
device.tap([(400, 400), (600, 600)])
# 设置按压力度 pressure, default == 100
device.tap([(400, 600)], pressure=50)

# 滑动
device.swipe([(400, 400), (600, 600)])

# 在使用完成后，需要显式调用stop方法将服务停止
device.stop()
