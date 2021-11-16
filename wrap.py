import sys

file = sys.argv[1]
width = int(sys.argv[2])
lines = open(file).readlines()
for i in lines:
    temp = i
    while len(temp) > width:
        print(temp[:width])
        temp = temp[width:]
    print(temp)

