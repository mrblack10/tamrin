def one_to_2D(list, r, c):
    output = []
    for row in range(0,r):
        out = []
        for col in range(0,c):
            if (row*c + col) < len(list):
                #print(list[row*c + col])
                out.append(list[row*c + col])
            else:
                out.append(None)
        output.append(out)
    return output

print(one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3))
