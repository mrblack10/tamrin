def crazy_list(my_list):
    #print (int(len(my_list)/2))
    for index in range(0,int(len(my_list)/2)):
        #print(my_list[index])
        if my_list[index] != my_list[len(my_list)-1-index] :
            return False
    return True

my_list = [5, 6, 8, 9, 9, 8, 6, 5]

print(crazy_list(my_list))
