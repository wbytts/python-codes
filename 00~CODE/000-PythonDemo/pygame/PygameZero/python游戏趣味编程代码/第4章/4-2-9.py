ball1 = [1, 2]  # 小球0的x，y坐标，也是一个列表
ball2 = [3, 4]  # 小球1的x，y坐标，也是一个列表
ball3 = [5, 6]  # 小球2的x，y坐标，也是一个列表

balls = []     # 空列表

# 将以上三个小球的位置列表，添加到balls中
balls.append(ball1)
balls.append(ball2)
balls.append(ball3)

# 输出列表balls中存储的小球元素的x，y坐标
for ball in balls: 
    print(ball[0], ball[1])