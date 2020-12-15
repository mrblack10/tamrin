def find_integer_with_most_divisors(mylist):
    def maqsom (x):
        s = 0
        for i in range(1,x+1):
            if (x % i) == 0 :
                #print(i,end = ',')
                s += 1
        #print("#end,s =",s)
        return s
    maax = 0
    maxitem = mylist[0]
    for item in mylist :
        #print('\n',item)
        if maax < maqsom(item) :
            maax = maqsom(item)
            maxitem = item
    return maxitem


mylist = [8, 12, 18, 6]

print(find_integer_with_most_divisors(mylist))
