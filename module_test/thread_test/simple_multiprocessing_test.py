from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(file_name):
    print("start to downloading, 进程号[%d]" % getpid())
    print("start to downloading %s..." % file_name)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s download completed. it spends %d seconds." % (file_name, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=("game of thrones_1",))
    p1.start()
    p2 = Process(target=download_task, args=("game of thrones_2",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("it all costs %.2f seconds." % (end-start))

if __name__ == '__main__':
    main()