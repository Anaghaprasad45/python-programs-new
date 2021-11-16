def min_max(l):
    min = max = l[0]
    for i in range(1, len(l)):
        if l[i] < min:
            min = l[i]
        if l[i] > max:
            max = l[i]
    return min, max


print("Min = %d Max = %d" % (min_max([9, 3, 10, 5, 6, 1])))
