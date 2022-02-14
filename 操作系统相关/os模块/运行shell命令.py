
import os

# 直接运行一条shell命令
os.system('calc')

# os.popen() 运行一条shell命令并读取其标准输出的文本，返回一个类文件对象
result = os.popen('dir')
print(result.read())
