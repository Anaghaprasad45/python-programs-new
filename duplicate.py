def dups(l1):
    a = l1[0]
    ans = []
    for i in l1:
        if a == i:
            if i not in ans:
                ans.append(i)
        a = l1[i]
    return ans


print(dups([1, 2, 1, 4, 2, 3, 5, 6, 5]))
