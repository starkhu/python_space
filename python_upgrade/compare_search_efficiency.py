# list的实现原理是应用数组完成的，因此，单词查询的时间复杂度是O(n)
# dict的实现原理是先对key生成一个hash, 再对hash生成一个红黑树进行查找， 时间复杂度O(logn)
# set的实现原理是用红黑树查找，时间复杂度O(logn)
# dict比set多一个hash的过程
# 查询效率：set > dict > list


import numpy as np
import datetime

def generateSourceData():
    rand_arr = np.random.randint(0, 10000000, 100000)
    print("type of rand_arr:", type(rand_arr))
    data_list = []
    data_dict = {}
    data_set = set()
    for i in range(len(rand_arr)):
        data_list.append(rand_arr[i])
        data_dict.setdefault(rand_arr[i], 1)
        data_set.add(rand_arr[1])
    return data_list, data_dict, data_set

def computeSearchTime(data_structure, structure_name):
    start = datetime.datetime.now()
    for i in range(10000):
        d = i in data_structure
    end = datetime.datetime.now()
    print(structure_name, "cost: ", (end-start), " seconds.")
    print(structure_name, "cost: ", (end - start).seconds, " seconds.")

def compareDataStructureDifference():
    data_list, data_dict, data_set = generateSourceData()
    computeSearchTime(data_set, "set")
    computeSearchTime(data_dict, "dict")
    computeSearchTime(data_list, "list")


if __name__ == "__main__":
    compareDataStructureDifference()
