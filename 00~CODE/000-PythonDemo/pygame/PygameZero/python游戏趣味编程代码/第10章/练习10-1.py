a = float(input('请输入数字a：'))
b = float(input('请输入数字b：'))

if (a>b):
    temp = a
    a = b
    b = temp

print('处理后a为：', a, ' b为：', b)
