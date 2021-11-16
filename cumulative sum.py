def cumulative_sum(list1):
    list2 = []
    sum = 0
    for i in list1:
        sum += i
        list2.append(sum)
    print(list2)


cumulative_sum([4, 3, 2, 1])
