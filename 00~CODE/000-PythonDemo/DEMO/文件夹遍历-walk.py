import os

for root, dirs, files in os.walk("d:/xiao_chen_maven_repo"):
    for file in files:
        print(root + "\\" + file)
        if file == "_remote.repositories":
            os.remove(root + "\\" + file)
