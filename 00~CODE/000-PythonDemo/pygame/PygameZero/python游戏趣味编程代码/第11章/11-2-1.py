grid = []  # 二维数组，开始为空列表
for i in range(2):  # 对行遍历
    row = []  # 存储一行的数据，开始为空列表
    for j in range(3):  # 对列遍历
        row.append(3*i+j)  # 把数据添加到行列表row中
    grid.append(row)  # 再把列表row添加到二维数组列表grid中

print(grid)  # 输出完整的二维数组
print(grid[0])  # 输出二维数组第0行
print(grid[0][1])  # 输出二维数组第0行第1列的元素值