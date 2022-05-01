import sys
from loguru import logger

# add()函数用于注册 “沉量”sink，用于管理日志消息。
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

# 可以用rotation、retention、compression进行日志窗口、更新、压缩管理。
logger.add("file_1.log", rotation="500 MB")    # 日志文件的窗口大小是500M
logger.add("file_2.log", rotation="12:00")     # 每天中午12点创建新日志文件
logger.add("file_3.log", rotation="1 week")    # 自动更新旧文件
logger.add("file_X.log", retention="10 days")  # 清理旧文件
logger.add("file_Y.log", compression="zip")    # 压缩文件



logger.debug("This's a new log message")



