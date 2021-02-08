import re

parser = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

def validate1(i, j, c, pwd):
    n = 0
    for k in pwd:
        if k == c:
            n += 1
    if n >= i and n <= j:
        return True
    return False

def validate2(i, j, c, pwd):
    return (pwd[i-1] == c) != (pwd[j-1] == c)

if __name__ == "__main__":
    valid1 = 0
    valid2 = 0
    with open('day02/input') as f:
        for line in f:
            m = parser.match(line)
            if m:
                i = int(m.group(1))
                j = int(m.group(2))
                c = m.group(3)
                password = m.group(4)
                if validate1(i, j, c, password):
                    valid1 += 1
                if validate2(i, j, c, password):
                    valid2 += 1
    print(f'Part1: {valid1}')
    print(f'Part2: {valid2}')
