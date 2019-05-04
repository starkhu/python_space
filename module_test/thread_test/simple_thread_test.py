from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print('start to download %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download completed. it cost %d seconds.' % (filename, time_to_download))

def main():
	start = time()
	t1 = Thread(target=download, args=('game of thrones_1',))
	t1.start()
	t2 = Thread(target=download, args=('game_of_thrones_2',))
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('it all costs %.3f seconds' % (end - start))


if __name__ == '__main__':
	main()