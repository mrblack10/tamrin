def unique_common(a, b):
    output=[]
    for item in a :
        if item in b and item not in output :
            output.append(item)
    if len(output)==0 :
        return None
    return sorted(output)


a = [5, 6, 7, 0]
b = [3, 2, 3, 2]

print(unique_common(a, b))
