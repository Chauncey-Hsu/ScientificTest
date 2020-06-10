import threading
# 成功运行

def run(param1, param2):
    while True:
        print("我是一个线程....." + param1)


# 创建一个线程，需要线程运行对的方法，并且给一个名称。
# 可以根据需求，给定参数
thread1 = threading.Thread(target=run("1","2"))

# 创建线程完毕之后，一定要启动
thread1.start()
