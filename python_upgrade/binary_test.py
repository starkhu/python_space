
def binaryTest():
    print(bin(12)) #10进制的二进制表示
    print("%i left remove 2 bit is %i" %(12, 0b1100 << 2)) #左移
    print("%i and %i do or operation is %i" %(0b1100, 0b1011, 0b11 | 0b1011)) #或操作
    print("%i and %i do or operation is %i" % (1, 14, 1 | 14))
    print("%i and %i do and operation is %b" % (1, 14, 1 & 14)) # 和操作
    print("%i and %i do XOR operation is %b" % (1, 14, 1 ^ 14))
    print(" %i do not operation is %b" % (12, ~12))


if __name__ == "__main__":
    binaryTest()