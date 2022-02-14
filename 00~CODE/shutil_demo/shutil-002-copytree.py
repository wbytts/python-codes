import shutil

# ignore_patterns(*patterns)： 忽略模式，用于配合copytree()方法，传递文件将会被忽略，不会被拷贝
# patterns：文件名称，元组

# copytree(src, dst, symlinks=False, ignore=None)： 拷贝文档树，将src文件夹里的所有内容拷贝至dst文件夹
'''
src：源文件夹
dst：复制至dst文件夹，该文件夹会自动创建，需保证此文件夹不存在，否则将报错
symlinks：是否复制软连接，True复制软连接，False不复制，软连接会被当成文件复制过来，默认False
ignore：忽略模式，可传入ignore_patterns()
copy_function：拷贝文件的方式，可以传入一个可执行的处理函数，默认为copy2，Python3新增参数
ignore_dangling_symlinks：sysmlinks设置为False时，拷贝指向文件已删除的软连接时，将会报错，如果想消除这个异常，可以设置此值为True
'''


# rmtree(path, ignore_errors=False, onerror=None)： 移除文档树，将文件夹目录删除
# ignore_errors：是否忽略错误，默认False
# onerror：定义错误处理函数，需传递一个可执行的处理函数，该处理函数接收三个参数：函数、路径和excinfo
