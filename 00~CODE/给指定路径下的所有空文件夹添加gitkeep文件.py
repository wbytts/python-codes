import os

path = r'E:\my-projects\obsidian-storage'

for dirpath, dirnames, files in os.walk(path):
    f = open(dirpath + '\\.gitkeep', 'w')
    f.flush()
    f.close()

