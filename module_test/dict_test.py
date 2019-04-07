
def one_line_test():
    a = "1;2;3"
    b = sorted(map(int, a.split(";")))
    print("type b:", type(b), "type b[0]:", type(b[0]))

def save_list_to_csv(one_list, list_name):
    # arr = np.array(one_list)
    # print("type of arr:", type(arr))
    # np.savetxt(list_name, arr, delimiter=',')
    file_out = open(list_name, 'a')
    file_out.write(str(one_list))
    file_out.close()

def dict_sort_test():
    dict = {'a': 2, 'b': 8, 'c': 4}
    sorted_dict = sorted(dict.items(), key=lambda e:e[1], reverse=True)
    save_list_to_csv(sorted_dict, "../data_space/dict_test.csv")
    sorted_dict1 = sorted(dict.items(), key=lambda e: e[1])
    save_list_to_csv(sorted_dict1, "../data_space/dict_test.csv")
    print(type(sorted_dict))
    print(sorted_dict)
    print(type(sorted_dict[0]))
    print(sorted_dict[0][0])

def dict_values_test():
    dict_1 = {"a": "Tom", "b": "Jacky", "c": "Pony"}
    v_l = dict_1.values()
    print(v_l)

def main():
    # one_line_test()
    dict_sort_test()
    #dict_values_test()

if __name__ == "__main__":
    main()