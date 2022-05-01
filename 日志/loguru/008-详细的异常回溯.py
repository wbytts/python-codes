from loguru import logger

logger.add("output.log", backtrace=True, diagnose=True)  # 设置为'False'可以保证生产中不泄露信息

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
