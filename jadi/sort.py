
my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]

def my_key(item):

    return item[0]                                            
new_sorted_list = sorted(my_list, key=my_key,reverse = True)                 
print("The sorted list looks like:", new_sorted_list)
