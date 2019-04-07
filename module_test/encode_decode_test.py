# -*- coding: utf-8 -*-

# 编码解码python版本和windows控制台都有关系。
# ASCII:单字节编码系统,ASCII(1~127)仅可代表英文、数字以及一些符号。
# unicode:通用编码，定长，为每种语言的每个字符设定了统一并且唯一的二进制编码，
#         以满足跨语言、跨平台进行文本转换、处理的需求。
# utf-8:针对unicode的可变成字符编码，它是unicode的实现方式之一，使用1-4个字节表示一个符号，
#        通常英文字母被编码成1个字节，常见汉字被编码成3个字节。
# gbk:是国标GB2312基础上扩容后的标准，双字节，包含中、英文字符。

# python2默认源代码是ASCII编码，故使用英文、数字情况下一切正常，使用英文后会报错
# 为了解决此问题，需要保存成utf-8的格式，通常需要在文件头加上如下标识：
#                     # -*- coding: utf-8 -*-
# 直接print中文显示为乱码，因为python编码成utf-8,windows控制台编码使用的是gbk,
# 故打印中文需要加上u'中文'
# python可以通过如下方式设置默认的encoding方式：
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python3.0开始所有字符串都支持unicode,默认保存为utf-8格式
# python3版本中，把'XXX'与u'XXX'统一编码成unicode编码，写不写前缀都一样

#python version must be 2.X
def python2BytesStrTest():
    if bytes == str:
        print("in python2, bytes are equal to str!")
    else:
        print("in python2, bytes are different to str!")

if __name__ == "__main__":
    python2BytesStrTest()