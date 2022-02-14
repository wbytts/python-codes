import os

# 遍历文件夹：将文件夹里的东西挨着找出来

"""
dirpath：文件夹路径
dirnames：文件夹下的子文件夹列表
file：文件夹下的文件列表
"""

for dirpath, dirnames, files in os.walk('f:/'):
    print(f'发现文件夹: {dirpath}')
    print('文件夹下的文件:', files)
    print('#' * 100)
