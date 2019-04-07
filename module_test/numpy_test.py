import numpy as np
import tensorflow as tf

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# endpoint=False means not include endpoint
# retstep=True means add step_length
def linspace_test():
    print(np.linspace(1, 10, 10))
    print(np.linspace(1, 10, 10, endpoint=False))
    print(np.linspace(1, 10, 10, retstep=True))

def sin_test():
    freq = 1000
    x = np.linspace(0, 2, 5)
    print("type of x:", type(x))
    print(x)
    y = np.sin(np.pi*x)
    print(y)
    print("type of y:", type(y))

def mean_test():
    #x = np.linspace(0, 2, 5)
    x = [[1, 2, 3], [4, 5, 6]]
    y = np.mean(x)
    print("mean y:", y)

def ceil_test():
    a = [-1.2, -0.7, -1, 0, 0.2, 2.3]
    y_round = [int(round(r))+10 for r in a]
    print(y_round)
    y_ceil = np.ceil(a)
    print(y_ceil)
    y_bytes = bytes(y_round)
    print(y_bytes)
    print("type of y_bytes: ", type(y_bytes))
    y_feature = tf.train.Feature(bytes_list=tf.train.BytesList(value=[y_bytes]))
    print("type of y_feature: ", type(y_feature))

def clip_test():
    a = [-11.2, -0.7, -13, 0 , 4.2, 1.3]
    y = np.clip(a, -2, 2)
    print(y)

def convert_between_list_and_array():
    one_list = [[1, 2, 3], [4, 5, 6]]
    list_to_array = np.array(one_list)
    array_to_list = list_to_array.tolist()
    print("type of list_to_array:", type(list_to_array))
    print(list_to_array)
    print("type of array_to_list:", type(array_to_list))

def reshape_test():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    b = arr.reshape([2, 6])
    # print(b)
    # print(b.shape)
    # print(arr.shape)
    for ele in b:
        print(ele)
    np.savetxt('reshape.csv', b, delimiter=',')

def mean_array_test():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    b = arr.reshape([2, 6])
    sum_array_b = None
    for ele in b:
        if sum_array_b is None:
            sum_array_b = ele
        else:
            sum_array_b += ele
    mean_array_b = sum_array_b / len(b)
    print(mean_array_b)

# load和save是numpy专用的二进制类型保存数据
def saveLoadDataTest():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    file_in = "../data_space/numpy_file.npy"
    np.save(file_in, arr)
    a = np.load(file_in)
    print(a)



def main():
    #linspace_test()
    #sin_test()
    #mean_test()
    #ceil_test()
    #clip_test()
    #convert_between_list_and_array()
    #reshape_test()
    #mean_array_test()
    saveLoadDataTest()

if __name__ == "__main__":
    main()

