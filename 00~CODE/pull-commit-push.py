import os

path = 'e:/my-projects'
dir_list = os.listdir(path)
print(dir_list)


for d in dir_list:
    dir_path = path + '/' + d
    temp_list = os.listdir(dir_path)
    if '.git' in temp_list:
        print(dir_path, '是一个git仓库')
        os.chdir(dir_path)
        os.system('git add .')
        os.system('git commit -m "update"')
        os.system('git pull')
        os.system('git add .')
        os.system('git commit -m "merge"')
        os.system('git push')


# 111
