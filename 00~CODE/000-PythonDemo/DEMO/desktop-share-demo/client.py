# _*_ coding:utf-8 _*_
import pythoncom
import socket
import os
import numpy
import cv2 as cv
from PIL import ImageGrab
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import threading


def jiep_recv(ip_port):
    socket_0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_0.bind((socket.gethostname(), ip_port))
    while True:
        try:
            img_data, address = socket_0.recvfrom(1024 * 1024)
        except Exception as e:
            cv.destroyAllWindows()
        else:
            # 申请内存块，并将收到的UDP数据放进内存块
            buf = BytesIO(img_data)
            # 将收到的UDP数据转为数组
            img_data = numpy.array(Image.open(buf))
            # 这一步作用重要，image类颜色格式为RGB，cv图片颜色格式为BGR故要将颜色格式进行转化，否则将色变
            img_data_1 = cv.cvtColor(img_data, cv.COLOR_RGB2BGR)
            img_data_1 = cv.resize(img_data_1, (850, 500), )
            # 显示图片
            cv.imshow("Service", img_data_1)
            buf.close()
            cv.waitKey(1)


def _winmains_():
    print(20 * "*" + "xxxx" + 20 * "*")
    port = int(input("请输入接收端口:"))
    if port > 65534:
        print("端口号过大！")
        return
    else:
        t1 = threading.Thread(target=jiep_recv, args=(port,))
        t1.start()


# 开发需要，用了一个新线程

if __name__ == '__main__':
    _winmains_()
