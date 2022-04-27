import threading
import time
import numpy
import cv2 as cv
from PIL import ImageGrab
from PIL import Image
from io import BytesIO
import socket

# 因为开发需要，我将接收端的IP与端口写进配置文件
ip_inifile = open("ip.ini", "r")
ipasport = ip_inifile.read()
ipAndport = ipasport.split(":")  # 拆分字符串
ip = ipAndport[0]  # 接收端IP
port = ipAndport[1]  # 接收端端口


def jiep_send():
    while True:
        ip_adder = (ip, int(port))
        # 截取桌面
        img = ImageGrab.grab()
        # 传输使用UDP协议，将图片分辨率变小方便传输，将ANTIALIAS作为第二个参数即可一定程度上提高画质
        out = img.resize((650, 400), Image.ANTIALIAS)
        # 申请一块内存块
        stram_0 = BytesIO()
        # 将图片以JPEG格式图片的方式保存至内存块
        out.save(stram_0, format='JPEG')
        # 将内存块当作图片文件打开，并转为数组
        jp_array = numpy.array(Image.open(stram_0))
        stram_0.close()
        # 再申请一个内存块
        stram_1 = BytesIO()
        pic = Image.fromarray(jp_array)
        # 将图片保存至新申请的内存块，以JPEG图片格式
        pic.save(stram_1, format='JPEG')
        # 提取内存块中的值
        jpeg = stram_1.getvalue()
        stram_1.close()
        # 设置UDP链接
        socket_0 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 是否正常发送
        try:
            socket_0.sendto(jpeg, ip_adder)
        # 断线重连机制，每三秒重拨一次
        except Exception as e:
            while True:
                try:
                    socket_0.sendto(jpeg, ip_adder)
                except Exception as e:
                    time.sleep(3)
                else:
                    break
        else:
            pass
        finally:
            socket_0.close()


def _winmain():
    # 因为开发需要我这里用了一个新线程来传输画面
    t1 = threading.Thread(target=jiep_send)
    t1.start()

if __name__ == '__main__':
    _winmain()

