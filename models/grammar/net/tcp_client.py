# client 客户端
# TCP必须建立连接
import socket  # 导入模块
import time


def revData(s):
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    print(data)
    print(" rev finished")


if __name__ == '__main__':
    # SOCK_STREAM---TCP协议方式
    # AF_INET----我的是ipv4地址
    # 1,创建socket对象：指定传输协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2，建立连接发送连接请求 ip地址和端口号
    s.connect(('127.0.0.1', 7890))
    s.send("fasdjlkfjsalfjls\r\n".encode())  # 只能发送字节流需要用encode转码字符串成字节，不然无法发送文件
    s.close()
    # revData(s)

    # TODO 有一个疑问就是 不知道发送什么什么会让对方觉得 if not rev_data 为终止，
    #  现在认为if not rev_data 要么作者不负责任，要么我还不了解。
    # if __name__ == '__main__':
    #     print(bool(int("0".encode().decode())))
    #
    # s.send(''.encode())

    # 被动的断开，比较合适。
    # s.send('exit'.encode())

