sum = 0
for i in range(100):
    x = float(input('请输入数字，输入负数结束：'))
    if (x>=0):
        sum += x
    else:
        break
print('输入正数的和为：',sum)