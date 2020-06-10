import socket
import threading
import time


def main():
    # 1.创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("", 7890))

    # 3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    # 循环目的：调用多次accept,从而为多个客户端服务
    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来(等待客户端的链接 accept)
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % str(client_addr))

        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink(new_client_socket, client_addr))
        t.start()

    # 如果将监听套接字 关闭了，那么会导致 不能再次等待新客户端的到来，即xxxx.accept就会失败
    tcp_server_socket.close()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        else:
            sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
            print('Hello, %s!' % data.decode('utf-8'))
    # 关闭套接字
    # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
    sock.close()
    print("已经为这个客户端服务完毕。。。。")


if __name__ == "__main__":
    main()
