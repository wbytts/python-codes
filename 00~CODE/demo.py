import time

target = 100
t = 0.2

for i in range(100):
    print('#' * i, end='')
    print(' ' * (target-i), end='')
    print(f':剩余时间：{(target - i) * t} 秒', end='')
    print('\r', end='')
    time.sleep(t)

print('#' * target, end='')
print(f':已完成', end='')
