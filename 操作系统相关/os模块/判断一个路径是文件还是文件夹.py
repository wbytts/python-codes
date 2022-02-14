import os

files = os.listdir()

for item in files:
    type = '文件夹' if os.path.isdir(item) else '文件'
    print(type, item)
