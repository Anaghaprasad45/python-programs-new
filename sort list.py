def lensort(l1):
    l1.sort(key=len)
    return l1


print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
