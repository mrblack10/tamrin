def formatted_print(mydict):
    l = list(mydict.items())
    l = sorted(l,key = lambda index : index[1],reverse = True)
    #print(l)
    for i in l:
        print("{:10s}{:6.2f}".format(i[0],i[1]))
        
    #print(l)



mydict = {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}

formatted_print(mydict)
