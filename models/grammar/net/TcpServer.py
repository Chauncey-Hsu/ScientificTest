import socket

# 这里的多线程与java类似，java如下：
#              while(true){
#                 // 调用accept()方法侦听，等待客户端的连接以获取Socket实例
#                 socket = serverSocket.accept();
#                 //创建新线程
#                 Thread thread = new Thread(new ServerThread(socket));
#                 thread.start();
#              }

def main():
    # 1. 创建套接字socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("", 7890))

    # 3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来(等待客户端的链接 accept)
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)  # 注意这个1024byte，大小根据需求自己设置
        print("客户端福送过来的请求是:%s" % recv_data.decode("utf-8"))

        # 回送一部分数据给客户端
        new_client_socket.send("hahahghai-----ok-----".encode("utf-8"))

        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
        new_client_socket.close()
        print("已经服务器完毕。。。。")

    # 如果将监听套接字 关闭了，那么会导致 不能再次等待新客户端的到来，即xxxx.accept就会失败
    tcp_server_socket.close()


if __name__ == "__main__":
    main()