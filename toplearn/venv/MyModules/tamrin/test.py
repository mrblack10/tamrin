i = [1, 2, 3, 4]
l = [4, 5, 6, 4, 7, 2, 10]
i += [t for t in l if t % 2 == 0 and t not in i]
print(i)
