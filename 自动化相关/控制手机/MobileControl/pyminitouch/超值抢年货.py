# 1080, 1920
from pyminitouch import MNTDevice

_DEVICE_ID = '91817db6'
device = MNTDevice(_DEVICE_ID)

i_range = int(1080 / 100)
j_range = int(1920 / 100)

while True:
    for i in range(1, i_range + 1):
        for j in range(1, j_range + 1):
            if j <= 2: continue
            device.tap([(100 * i, 100 * j)])

# 在使用完成后，需要显式调用stop方法将服务停止
device.stop()
