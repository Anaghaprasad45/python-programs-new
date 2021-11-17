import sys


def head(lines):
    for i in range(0, 10):
        print(lines[i])


def tail(lines):
    last = lines[-10:]
    for i in last:
        print(i)


file = sys.argv[1]
lines = open(file).readlines()
head(lines)
tail(lines)
