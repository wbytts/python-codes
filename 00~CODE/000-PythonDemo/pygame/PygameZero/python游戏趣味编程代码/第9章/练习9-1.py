X = [1,3,4,8,10]
number = 0
x = int(input('请输入数字：'))
if x <= X[0]:
    X.insert(0,x)
elif x >= X[4]:
    X.insert(5, x)
else:
    for i in range(4):
        if x >= X[i] and x <= X[i+1]:
            number = i+1
    X.insert(number, x)
print('插入后的列表为：',X)