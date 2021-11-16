# def reverse(list1):
#     list1.reverse()
#     return list1
#
#
# print(reverse(reverse([2, 3, 1])))

l1 = [2, 1, 4, 8]
l2 = []
for i in range((len(l1)-1), -1, -1):
    l2.append(l1[i])
print(l2)
