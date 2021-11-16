def count_digits(x):
    count = 0
    while x != 0:
        count += 1
        x = x // 10
    return count


print(count_digits(123456))
