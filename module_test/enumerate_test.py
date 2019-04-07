def enumrateTest():
    l = ["this", "is", "my", "space"]
    for index, item in enumerate(l):
        print(index, ", ", item)
    for index, item in enumerate(l, 2):
        print(index, ", ", item)


if __name__ == "__main__":
    enumrateTest()