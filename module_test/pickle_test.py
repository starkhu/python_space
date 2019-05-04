import pickle as p

# 对python对象进行序列化操作，所谓序列化即将python对象转换成某种格式的文件保存在本地，
# 并且能够通过load操作完全可逆的回复保存的对象信息
#
#json模块也能对文件进行序列化和反序列化。
def dumpTest():
    fruit_list = ["apple", "mango", "carrot", "香蕉"]
    file_out = "../data_space/fruit.pkl"
    fw = open(file_out, "wb")
    p.dump(fruit_list, fw)
    fw.close()

def loadTest():
    file_in = "../data_space/fruit.pkl"
    fi = None
    try:
        fi = open(file_in, "rb")
    except FileNotFoundError:
        print("input file not found!")

    finally:
        if fi:
            fruit_list = p.load(fi)
            print(fruit_list)

if __name__ == "__main__":
    #dumpTest()
    loadTest()