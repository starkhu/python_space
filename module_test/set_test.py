
def createSet():
    set1 = {"apple", "banana", "car"}
    set2 = set(["apple", "banana", "car"])
    # print(set1, " ", type(set1))
    # print(set2, " ", type(set2))
    if set1 == set2:
        print("the results of two created collections are consistent")
    else:
        print("the results of two created collections are different")
    return set1

def createFrozenSet():
    set1 = frozenset({"apple", "banana", "car"})
    try:
        set1.add("duck")
    except:
        print("frozen set can not do add op.")

def commonOperationTest(s):
    add_op = s.add("duck")
    remove_op = s.remove("apple")
    print(s)


if __name__ == "__main__":
    # createSet()
    # commonOperationTest(createSet())
    createFrozenSet()