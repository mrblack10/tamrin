def find_gcd(my_list):
    for i in range(min(my_list),0,-1):
        t = True
        print("i:",i,end=" ----> ")
        for item in my_list :
            print(item,end = ',')
            if (item % i) != 0:
                t = False
                break
        print()
        if t :
            return i

my_list = [3, 5, 9, 11, 13]

print(find_gcd(my_list))
