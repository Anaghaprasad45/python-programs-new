f = open("she.txt", 'w')
f.writelines("""She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.""")
f.close()
a = open("she.txt").readlines()
print(a[::-1])