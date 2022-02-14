import os
import pickle
import time

data = pickle.load(open('data.pickle', 'rb'))
target_dir = 'e:\\code\\'

paths = list(data.keys())
path = sorted(paths)

for p in paths:
    print(p)
    target_path = p.replace('e:/', target_dir)
    # try:
    with open(target_path, 'wb') as f:
        f.write(data[p])
    # except:
    #     target_dir = '/'.join(target_path.split('\\')[:-1]).replace('/', '\\')
    #     os.system(f'mkdir {target_dir}')



