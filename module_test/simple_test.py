a = 21
b = 3
c = a if a<b else b
print(c)
while 1<2-99999:
    print("lal")

path = "E:\\mini_project\\python_test\\module_test\\map_test.py"

f = path.strip().split("\\")[-1].split(".")[0]
print(f, f.find("testa"))
if f.find("tests") != -1:
    print("founnd")


    b = os.path.abspath(a)
    print(b)
    if os.path.exists(a):
        print("exists")