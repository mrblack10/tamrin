def list_of_primes(n):
    mylist = [2]
    for i in range(3,n,2):
        #print(i)
        t = True
        for  item in mylist :
            if i % item == 0 :
                t = False
                break
        if t == True :
            mylist.append(i)
    #print("list adad aval 1 ta",n,":",end = '')
    return mylist

print(list_of_primes(30))
