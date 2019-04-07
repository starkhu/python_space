def list_replace_test():
    l = ["a", "s", "d"]
    l.remove("a")
    l.append("q")
    for i in l[-2:]:
        print(i)

def convert_between_list_and_array():
    one_list = [[1, 2, 3], [4, 5, 6]]
    list_to_array = np.array(one_list)
    array_to_list = list_to_array.tolist()
    print("type of list_to_array:", type(list_to_array))
    print(list_to_array)
    print("type of array_to_list:", type(array_to_list))

def list_multiply_test():
    a = [0]
    b = a * 3
    print(type(b), " ", len(b))
    print(b[0])
    print()

#列表分片
def simple_express_test():
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s_l = list1[0:9:2]
    print(s_l)

#列表的倒序

def main():
    #list_replace_test()
    #list_multiply_test()
    #simple_express_test()
    mapTest()


if __name__ == "__main__":
    main()