def MY_2D_LIST(n):
    output = [[1]]
    for i in range(1,n):
        my_list = [1]
        for j in range(1,i):
            my_list.append(output[i-1][j-1] + output[i-1][j])
        my_list.append(1)
        output.append(my_list)
    return output

print(MY_2D_LIST(2))
