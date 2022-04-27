absMax = 0
number = 0
print("请依次输入5个数字")
for i in range(5):
    x = int(input("请输入数字："))
    if abs(x) > absMax:
        absMax = abs(x)
        number = x
print("绝对值最大的数字是："+str(number))