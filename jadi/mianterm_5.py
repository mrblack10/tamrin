def items_price(a, b):
    s = 0
    for index in range(len(a)) :
        s += a[index] * b[index]

    return s










a = [2, 3, 5, 7, 9]


b = [5, 8, 4, 1, 11]

print(items_price(a, b))
