import sys

file = sys.argv[1]
lines = open(file).readlines()
for i in lines:
    print(i.center(150))
