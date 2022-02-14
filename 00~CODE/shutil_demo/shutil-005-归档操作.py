import shutil

'''
make_archive(base_name, format, root_dir, …)： 生成压缩文件
    base_name：压缩文件的文件名，不允许有扩展名，因为会根据压缩格式生成相应的扩展名
    format：压缩格式
    root_dir：将制定文件夹进行压缩

get_archive_formats()： 获取支持的压缩文件格式。目前支持的有：tar、zip、gztar、bztar。在Python3还多支持一种格式xztar

unpack_archive(filename, extract_dir=None, format=None)： 解压操作
    filename：文件路径
    extract_dir：解压至的文件夹路径。文件夹可以不存在，会自动生成
    format：解压格式，默认为None，会根据扩展名自动选择解压格式

get_unpack_formats()： 获取支持的解压文件格式。目前支持的有：tar、zip、gztar、bztar和xztar
'''

