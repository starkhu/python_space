import tqdm

def yieldGenerator():
    data = []
    for i in range(0, 100, 2):
        data.append(i)
        if len(data) == 3:
            yield  data
            data = []

def yieldTest():
    data_iter = yieldGenerator()
    print(type(data_iter))
    for i in data_iter:
        print(i)

if __name__ == "__main__":
    yieldTest()