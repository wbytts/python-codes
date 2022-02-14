"""
当变量内容改变时，执行指定的回调

变动追踪：x.trace('w', callback)：w表示写入操作
读取追踪：x.trace('r', callback)：r表示读取操作

callback的参数：
    1. tk变量名称
    2. index索引
    3. mode模式
    目前不怎么用参数，所以写成 *args 然后不用就好了
"""
