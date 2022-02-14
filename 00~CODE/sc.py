import os
import pickle

root_dir = 'e:/projects'
projects = os.listdir(root_dir)
data = {}

for project in projects:
    if project in ['.nvimlog']: continue
    dirs = os.listdir(root_dir + '/' + project)
    print(dirs)
    for dir in dirs:
        if dir in ['.git', 'node_modules']: continue
        for root, ds, files in os.walk(root_dir + '/' + project + '/' + dir):
            for file in files:
                print(os.path.join(root, file))
                filename = os.path.join(root, file)
                with open(filename, 'rb') as f:
                    content = f.read()
                    data[filename] = content


pickle.dump(data, open('data.pickle', 'wb'))


# for root, dirs, files in os.walk(r"D:\test"):
#     for file in files:
#         #获取文件所属目录
#         print(root)
#         #获取文件路径
#         print(os.path.join(root,file))
