
def write_to_file():
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    with open("../data_space/write_test.csv", 'a') as fw:
        fw.write("%d,%d,%d\n" % (a[0], a[1], a[2]))
        fw.write("%s,%s,%s\n" % (b[0], b[1], b[2]))
        fw.close()

def main():
    write_to_file()

if __name__ == "__main__":
    main()