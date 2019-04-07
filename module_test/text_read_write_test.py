# -*- coding: utf-8 -*-
from tqdm import tqdm

def write_to_file_test():
   str1 = u'今天是个好日子，因吹斯听'
   str2 = u'大河之水天上来'
   str_list = [str1, str2]
   file_out = "../data_space/write_test.txt"
   with open(file_out, "wb") as fw:
       for line in str_list:
           line_bytes = bytes(line, encoding="utf8")
           fw.write(line_bytes)
           fw.write("\r\n".encode("utf8")) # endline
   #fw.close()

#common way to read files
def read_from_file_test():
    file_in = "../data_space/write_test.txt"
    with open(file_in, 'rb') as fr:
        for line in fr.readlines():
            print("type of origin line", type(line))
            line = str(line, encoding="utf-8")
            print("len of line:", len(line))
            print(line)
            line = line.strip()
            print("len of line:", len(line))
            print(line)

# perfect way to read big_file
# automatic use of IO cache and management memory
def read_from_bigfile_test():
    file_in = "E:\\mini_project\\tencent_word2vec\\Tencent_AILab_ChineseEmbedding.txt"
    read_num = 0
    with open(file_in, 'rb') as fr:
        for line in tqdm(fr):
            line = str(line, encoding="utf-8")
            # if read_num >= 10:
            #     break
            # else:
            #     read_num += 1
            #     print(read_num, ": ", line)


def main():
    # write_to_file_test()
    # read_from_file_test()
    #read_from_bigfile_test()

if __name__ == "__main__":
    main()