from watchdog.observers import Observer
from watchdog.events import *
import time
import os

'''
此脚本用来自动格式化node项目中的代码
需要项目中安装了 prettier
并且配置了配置文件
'''


class MyHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path

    def on_modified(self, event):
        print("文件被修改了 %s " % event.src_path)
        os.chdir(self.path)
        os.system('prettier --write ./src/**/*.{js,ts,vue,scss,json}')


if __name__ == "__main__":
    paths = [
        r"F:\work\code\delivery-mobile",
        r"D:\projects\Vue\delivery-service"
    ]

    os.system('npm install prettier -g')

    os.system('title 格式')
    obs = []
    for p in paths:
        event_handler = MyHandler(p)
        observer = Observer()
        observer.schedule(event_handler, p, recursive=True)
        observer.start()
        obs.append(observer)

    try:
        while True:
            time.sleep(0.001)

    except KeyboardInterrupt:
        for ob in obs:
            ob.stop()

    for ob in obs:
        ob.join()
