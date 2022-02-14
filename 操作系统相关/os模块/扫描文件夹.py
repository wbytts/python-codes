import os

print(os.scandir())

for item in os.scandir():
    # print(item)
    print(f'''文件名称：{item.name}
文件路径：{item.path}
是否是文件夹：{item.is_dir()}
{'#' * 100}''')

"""
<nt.ScandirIterator object at 0x00000276DA35FD50>
<DirEntry '判断一个路径是文件还是文件夹.py'>
<DirEntry '执行操作系统命令.py'>
<DirEntry '扫描文件夹.py'>
<DirEntry '拼接路径（平台无关）.py'>
<DirEntry '获取当前脚本运行的路径.py'>
<DirEntry '输出目录下所有的文件夹和文件.py'>
"""
