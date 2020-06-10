# coding=utf-8
# @Auther : "鹏哥贼优秀"
# @Date : 2019/8/10
# @Software : PyCharm 

from multiprocessing import Pool
import time
import threading


# 多进程的写数据方法
def writedata(content):
    with open("new1.txt", "a") as f:
        f.writelines(content)


# 定义自己的多线程继承类
class myThread(threading.Thread):
    # 声明myThread是多线程的继承类
    def __init__(self, content):
        threading.Thread.__init__(self)
        self.content = content

    # 多线程运行的内容
    def run(self):
        threadingLock = threading.Lock()
        threadingLock.acquire()
        self.my_writedata(self.content)
        threadingLock.release()

    # 多线程的写数据方法
    def my_writedata(self, content):
        with open("new2.txt", "a") as f:
            f.writelines(content)


if __name__ == "__main__":
    # 创建一个test.txt，用于数据读取后的写入
    with open("test.txt", "w")as f_w:
        for i in range(1000):
            f_w.write(str(i) + "\n")
    # 多进程读写
    print("开始计时(多进程写入)")
    t0 = time.time()
    with open("test.txt", "r", encoding="utf-8")as f:
        content = f.readlines()
    pool = Pool(processes=4)
    pool.map_async(writedata(content), range(len(content)))
    pool.close()
    pool.join()
    t1 = time.time()
    print("完成时间为：{0}".format(t1 - t0))
    # 多线程读写
    print("开始计时(多线程写入)")
    t2 = time.time()
    with open("test.txt", "r", encoding="utf-8")as f:
        content = f.readlines()
    threads = []
    threadnum = 4
    eline = len(content) // threadnum
    for i in range(threadnum):
        threadtemp = myThread(content[i * eline:(i + 1) * eline])
        threadtemp.start()
        threads.append(threadtemp)
    for i in threads:
        i.join()
    t3 = time.time()
    print("完成时间为：{0}".format(t3 - t2))