# unique using set

"""def unique(l1):
    return set(l1)


print(list(unique([1, 2, 1, 3, 2, 5])))"""


# another way

def unique(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2


print(unique([1, 2, 2, 3, 4, 1, 4, 6, 7]))



