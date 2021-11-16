f = open("sample.txt", "w")
f.write("python programming")
f.close()
line = open("sample.txt").read()
print(line[::-1])



