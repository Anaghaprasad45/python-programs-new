import sys


def head(lines):
    for i in range(0, 10):
        print(lines[i])


file = sys.argv[1]
lines = open(file).readlines()
head(lines)


