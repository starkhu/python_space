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
    print("####")
    data_list, data_dict, data_set = generateSourceData()
    print("####")
    computeSearchTime(data_set, "set")
    computeSearchTime(data_dict, "dict")
    computeSearchTime(data_list, "list")


if __name__ == "__main__":
    compareDataStructureDifference()
