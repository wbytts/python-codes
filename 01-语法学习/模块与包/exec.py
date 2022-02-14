
'''
使用exec运行模块文件：
    exec( open('xxx.py').read() )

exec(s)：执行字符串存储的python代码
    独立执行，不会寻找字符串以外的语法
    （与eval一样，也有globals和locals参数）

exec也有着类似于import的效果，但它实际上不会真的导入模块
exec的工作机制就好像在调用它的地方粘贴了代码一样（有可能默默地覆盖掉当前正在使用的变量）
'''
