def multiplication_table(n):
    list2 = []
    for i in range(1,n+1):
        list = []
        for j in range(i,n*i+1,i):
            list.append(j)
        list2.append(list)
    return list2

print(multiplication_table(4))
