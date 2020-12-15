def row_maximums(list):
    dict={}
    for row in range(len(list)) :
        s = 'row '+str(row)+' max' 
        dict[s] = max(list[row])
    return dict


list = [[5, 0, 0, 0, 13],
        [0, 12, 0, 0],
        [20, 0, 11, 0],
        [6, 0, 0, 8]]

print(row_maximums(list))
