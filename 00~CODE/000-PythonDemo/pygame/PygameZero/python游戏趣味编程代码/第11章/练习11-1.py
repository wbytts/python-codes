import random  # 导入随机库

grid = []  # 二维数组，开始为空列表
for i in range(5):  # 对行遍历
    row = []  # 存储一行的数据，开始为空列表
    for j in range(5):  # 对列遍历
        row.append(random.randint(1, 6))  # 把数据添加到行列表row中
    grid.append(row)  # 再把列表row添加到二维数组列表grid中

print('随机二维数组：')
for i in range(5):  # 对行遍历
    s = ''
    for j in range(5):  # 对列遍历
        s = s + str(grid[i][j]) + '  '
    print(s)

for i in range(5):  # 对行遍历
    for j in range(5):  # 对列遍历
        if (grid[i][j] == 6):
            grid[i][j] = 0

print('处理后的二维数组：')
for i in range(5):  # 对行遍历
    s = ''
    for j in range(5):  # 对列遍历
        s = s + str(grid[i][j]) + '  '
    print(s)
