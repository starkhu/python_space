import re

def matchTest():
    a = "hello python, so cold[haha]"
    b = re.search(r"\[.*\]", a)
    print("b: ", b)
    if b is not None:
        target_start = b.start()
        target_end = b.end()
        print(target_start, " ", target_end)

def repalceTest():
    sentence = "你个大傻叉，二货，坑队友,shit,Shit"
    purified = re.sub('傻[子叉比]|二[货比B]|shit', '*', sentence, flags=re.IGNORECASE)
    print(purified)

def splitTest():
    poem = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
    poem_list = re.split(r'[，。,.]', poem)
    print(poem_list)
    while '' in poem_list:
        poem_list.remove('')
    print(poem_list)
if __name__ == "__main__":
    #matchTest()
    #repalceTest()
    splitTest()