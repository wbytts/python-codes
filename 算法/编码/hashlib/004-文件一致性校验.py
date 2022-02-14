'''
下载一个软件时，往往都带有一个MD5或者shax值，当下载完成这个应用程序时你要是对比大小根本看不出什么问题，
应该对比它们的md5值，如果两个md5值相同，就证明这个应用程序是安全的，如果你下载的这个文件的MD5值与服务端给你提供的不同
，那么就证明你这个应用程序肯定是植入病毒了（文件损坏的几率很低），那么应该赶紧删除。
'''


# python-3.6.6-amd64.exe 文件检验
f = open(r"F:\s24\day17\python-3.6.6-amd64.exe","rb")
import hashlib
md5 = hashlib.md5()
while True:
    msg = f.read(1024)
    if msg:
        md5.update(msg)
    else:
        print(md5.hexdigest())
        break
# 767db14ed07b245e24e10785f9d28e29   结果一样说明ok的


