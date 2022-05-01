import logging

"""
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

------
%(name)s            Name of the logger (logging channel)
%(levelno)s         Numeric logging level for the message (DEBUG, INFO,WARNING, ERROR, CRITICAL)
%(levelname)s       Text logging level for the message ("DEBUG", "INFO","WARNING", "ERROR", "CRITICAL")
%(pathname)s        Full pathname of the source file where the loggingcall was issued (if available)
%(filename)s        Filename portion of pathname
%(module)s          Module (name portion of filename)
%(lineno)d          Source line number where the logging call was issued(if available)
%(funcName)s        Function name
%(created)f         Time when the LogRecord was created (time.time() return value)
%(asctime)s         Textual time when the LogRecord was created
%(msecs)d           Millisecond portion of the creation time
%(relativeCreated)d Time in milliseconds when the LogRecord was created,relative to the time the logging module was loaded (typically at application startup time)
%(thread)d          Thread ID (if available)
%(threadName)s      Thread name (if available)
%(process)d         Process ID (if available)
%(message)s         The result of record.getMessage(), computed just as the record is emitted
"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)
