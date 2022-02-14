import shutil
'''
move(src, dst)：
    将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst
    若dst目录存在，将会把src文件夹的所有内容移动至该目录下面
        src：源文件夹或文件
        dst：移动至dst文件夹，或将文件改名为dst文件。如果src为文件夹，而dst为文件将会报错
        copy_function：拷贝文件的方式，可以传入一个可执行的处理函数。默认为copy2，Python3新增参数
'''
