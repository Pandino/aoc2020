if __name__ == "__main__":
    data = set()
    with open('day01/input.txt') as f:
        for line in f:
            data.add(int(line))
    for i in data:
        j = 2020 - i
        if j > 0:
            for z in data:
                if j - z in data:
                    print(z, j-z, i)
                    print(z * (j-z) * i)