x = int(input('请输入0-100的得分：'))
if (90<=x<=100):
    print('优秀')
elif (80 <= x < 90):
    print('良好')
elif (70 <= x < 80):
    print('中等')
elif (60 <= x < 70):
    print('及格')
else:
    print('不及格')