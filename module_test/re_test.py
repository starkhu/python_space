import re

def matchTest():
    a = "hello python, so cold[haha]"
    b = re.search(r"\[.*\]", a)
    print("b: ", b)
    if b is not None:
        target_start = b.start()
        target_end = b.end()
        print(target_start, " ", target_end)

if __name__ == "__main__":
    matchTest()