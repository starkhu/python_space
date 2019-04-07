# -*- coding: utf-8 -*-
#map()函数会根据提供的序列对指定的序列做映射
#map(function, iterable,……)

#python2中可以直接打印出结果
#python3需要加上list(map())才能打印出相应的结果

def square(x):
    return x ** 2

#python2
# def mapTest_python2():
#     a = map(square, [1, 2, 3, 4, 5])
#     print a
#     b = map(lambda x: x % 2, range(7))
#     print b

#python3
def mapTest_python3():
    a = map(square, [1, 2, 3, 4, 5])
    a = list(a)
    print(a)
    b = map(lambda x: x % 2, range(7))
    b = list(b)
    print(b)
    c = "E:\\mini_project\\audio_classification\\Youtube-8M-WILLOW-master\\mp4\\q0620i8ftku.mp4"
    c = list(map(ord, c))
    print(c,  "\n", len(c))

#ord: 字符对应的ASCII码
#chr: ASCII码对应的字符
def ordChrTest():
    s = "abcdefg"
    ord_s = list(map(ord, s))
    print(ord_s)
    chr_s = list(map(chr, ord_s))
    print(chr_s)

if __name__ == "__main__":
    #mapTest_python2()
    #mapTest_python3()
    ordChrTest()