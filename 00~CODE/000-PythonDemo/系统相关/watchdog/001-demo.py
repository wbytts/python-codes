import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # 配置日志格式
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # 定义监控的路径
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = r'D:/'
    # 初始化日志处理器
    event_handler = LoggingEventHandler()
    # 初始化观察
    observer = Observer()
    # 设置计划任务
    observer.schedule(event_handler, path, recursive=True)
    # 启动
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



