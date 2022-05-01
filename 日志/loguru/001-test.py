from loguru import logger

"""
loguru的用法非常简单，在 loguru 中有且仅有一个对象：logger。
为了使用方便，logger在使用时，是提前配置好的，
并且开始是默认输出至stderr（但是这些完全是可以再进行配置的），
而且打印出的log信息默认是配置了颜色的。
"""

logger.debug("This's a log message")
