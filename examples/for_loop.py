def read_data():
    f = open("data.txt")
    return f.read()

for _ in range(10_000):
    print(read_data())
