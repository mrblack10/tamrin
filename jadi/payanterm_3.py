def n_letter_dictionary(my_string):
    my_dict = {}
    my_string = my_string.lower().split(' ')
    len_list = []
    for item in my_string :
        len_list.append(len(item))
    len_list.sort()
    for my_len in len_list :
        my_dict[my_len] = []
    for item in my_string :
        if item not in my_dict[len(item)]:
            my_dict[len(item)].append(item)
            my_dict[len(item)].sort()
    return my_dict



my_string = "The way you see people is the way you treat them and the Way you treat them is what they become"


print(n_letter_dictionary(my_string))
