import pandas as pd

def save_to_csv_test():
    a = [1, 2, 3]
    b = [4, 5, 6]
    key = ['a_name', 'b_name']
    test_dict = {}
    test_dict[key[0]] = a
    test_dict[key[1]] = b
    #dataframe = pd.DataFrame({'a_name':a, "b_anme":b})
    dataframe = pd.DataFrame(test_dict)
    dataframe.to_csv('../data_space/test.csv', index=False, sep=',')

if __name__ == "__main__":
    save_to_csv_test()