#当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间
#所以即使counter是全局变量，每个子进程都会有一个counter变量。
#如果想要实现进程间通信，可以通过管道或者信号量等机制实现。

from multiprocessing import Process
from time import sleep

counter = 0

def sub_task(string):
    global counter
    while counter < 3:
        print(string)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task, args=('Hello',)).start()
    Process(target=sub_task, args=('Python',)).start()

if __name__ == '__main__':
    main()