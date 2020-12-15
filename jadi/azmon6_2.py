def list_to_tuples(list2):
    output = []
    for l in range(len(list2)) :
        list2[l].reverse()
        list2[l] = tuple(list2[l])
        output.append(list2[l])
    return tuple(output)




list2 = [['mean', 'really', 'is', 'jean'],
        ['world', 'my', 'rocks', 'python']
    ]

print(list_to_tuples(list2))
        
    
