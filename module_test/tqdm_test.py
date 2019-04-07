from tqdm import tqdm
import time

# Tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加
# 一个进度提示信息，用户只需要封装任意的迭代器 tqdm(iterator)。
def tqdmTest():
    for i in tqdm(range(10000)):
        time.sleep(0.01)


if __name__ == "__main__":
    tqdmTest()
