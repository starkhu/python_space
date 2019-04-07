import os

def path_test():
    a = "E:\\mini_project\\function_test\\out1.wav"
    b = os.path.abspath(a)
    print(b)
    if os.path.exists(a):
        print("exists")
    c = os.path.dirname(a)
    print(c)

def file_exist_test():
    a = "E:\\mini_project\\python_test\\data_space_out1.wav"
    b = "E:\\mini_project\\python_test\\data_spae_out2.wav"
    if os.path.exists(a):
        print("out1.wav exists")
    if os.path.exists(b):
        print("out2.wav exists")

def get_file_name():
    a = "E:\\mini_project\\function_test\\out1.wav"
    b = a.split("\\")[-1].split('.')[0]
    print(b)

def get_file_ext():
    file_1 = "E:\mini_project\python_test\module_test\encode_decode_test.py"
    name, ext = os.path.splitext(file_1)
    print(name)
    print(ext)


if __name__ == "__main__":
    path_test()
    #file_exist_test()
    #get_file_name()
    #get_file_ext()

