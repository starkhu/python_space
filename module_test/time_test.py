import time


def time_test():
    ticks = time.time()
    print("current timestamp is: ", ticks)

def localtime_test():
    localtime = time.localtime(time.time())
    print("local time is: ", localtime)

def asctime_test():
    asctime = time.asctime(time.localtime(time.time()))
    print("asctime is:", asctime)

def strftime_test(): #self define time format
    strftime = time.strftime("%Y-%M-%D %H:%M:%S %a %b")
    print("strftime is: ", strftime)

def formattime_to_timestamp():
    # a = "Sat Dec 29 10:37:00 2018"
    # timestamp = time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
    t_20181228_start = "2018 12 1 00:00:00"
    timestamp_20181228_start = time.mktime(time.strptime(t_20181228_start, "%Y %m %d %H:%M:%S"))
    t_20181228_end = "2018 12 28 23:59:59"
    timestamp_20181228_end = time.mktime(time.strptime(t_20181228_end, "%Y %m %d %H:%M:%S"))
    print("20181228_start_timestamp is: ", timestamp_20181228_start)
    print("20181228_end_timestamp is: ", timestamp_20181228_end)


def main():
    time_test()
    localtime_test()
    asctime_test()
    strftime_test()
    formattime_to_timestamp()


if __name__ == "__main__":
    main()