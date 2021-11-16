import sys

file = sys.argv[1]
string = sys.argv[2]
line = open(file).readlines()
for i in line:
    if string in i:
        print(i)
