#gfile即google_file，是谷歌公司自己开发的关于文件的操作函数，
#gfile函数的许多功能和os.path模块很类似

from tensorflow import gfile

def GlobTest():
    file_name = "E:\\mini_project\\python_test\\module_test\\tf_test\\data_space"
    file = gfile.Glob(file_name)
    print(file)

if __name__ == "__main__":
    GlobTest()