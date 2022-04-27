import socket

if __name__ == '__main__':
    # 创建TCP客户端套接字
    # socket.AF_INET 表示IPV4的地址类型
    # socket.SOCK_STREAM 表示TCP的传输协议
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 和服务端套接字建立连接
    client.connect(('192.168.1.5', 8987))

    # 发送数据到服务端
    send_content = 'hello!!! 你好啊！'
    send_data = send_content.encode('gbk')
    client.send(send_data)

    # 接收数据, 这次接收的数据最大字节数是1024
    recv_data = client.recv(1024)
    # 返回的直接是服务端程序发送的二进制数据
    print(recv_data)
    # 对数据进行解码
    recv_content = recv_data.decode("gbk")
    print("接收服务端的数据为:", recv_content)

    # 关闭套接字
    client.close()