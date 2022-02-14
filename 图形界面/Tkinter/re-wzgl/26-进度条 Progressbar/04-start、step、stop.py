"""
start(interval)：每个interval时间移动一次指针，interval默认值是50ms，每次指针移动调用一次 step(delta)

step(delta)：每次增加一次 delta，默认值是 1.0
             在 determinate 模式，指针不会超过 maximum 参数值
             在 indeterminate 模式，当指针达到 maximum 参数值前一格时，指针会回到起点

stop()：停止 start() 的运行
"""

