def calculate_expenses(filename):
    myfile = open(filename,'r')
    data = myfile.readlines()
    mydict = {}
    for line in range(len(data)) :
        data[line] = data[line].strip().split(',')
        for item in range(len(data[line])):
            data[line][item] = data[line][item].strip()
        if data[line][0] not in mydict.keys():   
            mydict[data[line][0]] = float(data[line][1])
        else:
            mydict[data[line][0]] += float(data[line][1])
    output = list(mydict.items())
    output = sorted(output,key = lambda index : index[0])
    #print(output)
    for i in range(len(output)) :
        #print(output[i][1])
        l = list(output[i])
        #print(l)
        l[1] = "${:.2f}".format(l[1])
        #print(l[1])
        output[i] = tuple(l)
    return output
            
    

print(calculate_expenses('azmon6_5.txt'))

    
