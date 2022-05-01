import logging  # 引入logging模块，将信息打印到控制台上

# 1、logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)

# 2、由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
