import shutil

# shutil.copyfile(原文件路径, 目标文件路径)
shutil.copyfile('e:/temp/a.txt', 'e:/temp/b.txt')

# shutil.copyfileobj(原文件对象, 目标文件对象, length=缓冲区大小)
# f1 = open('a.txt', 'r')
# f2 = open('b.txt', 'w')
# shutil.copyfileobj(f1, f2)


# shutil.copymode(src, dst, follow_symlinks=True)：复制文件权限
# follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限，如果设置为True，则当成普通文件复制权限

# shutil.copystat(src, dst, follow_symlinks=True)：复制权限，上次访问时间，上次修改时间以及src的标志
# follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限、上次访问时间，上次修改时间以及src的标志，如果设置为True，则当成普通文件复制权限


# shutil.copy(src, dst, follow_symlinks=True)：将文件src复制至dst
# dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件
# 权限会被一并复制

# shutil.copy2(src, dst, follow_symlinks=True)
# 与 copy 的区别是，权限、上次访问时间、上次修改时间和src的标志会一并复制至dst





