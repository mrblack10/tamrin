def create_grades_dict(file_name):
    myfile = open(file_name,'r')
    data = myfile.readlines()
    mydict = {}
    #print(data)
    for line in range(len(data)) :
        data[line] = data[line].strip().split(',')
        a = 1
        t = [0,0,0,0,0]
        for i in range(len(data[line])) :
            #print("i :",i,end=' --> ')
            data[line][i] = data[line][i].strip()
            #print (data[line][i])
            if "Test_" in data[line][i] and int(data[line][i][5])<=4:
                t[int(data[line][i][5])] = int(data[line][i+1])
            
        #print("dataline:",data[line])
        mydict[data[line][0]] = [data[line][1],t[1],t[2],t[3],t[4],sum(t)/4]
        #print(mydict[data[line][0]],"\n*****************")
        
    return mydict
    
#######################################################################################


def print_grades(file_name):
    print("{:^10s} | {:^16s} | {:^6s} | {:^6s} | {:^6s} | {:^6s} | {:^6s} |".format("ID","Name","Test_1","Test_2","Test_3","Test_4","Avg."))
    mydict = create_grades_dict(file_name)
    listkeys = sorted(list(mydict.keys()))
    for ID in listkeys :
        print("{:10s} | {:16s} | {:6d} | {:6d} | {:6d} | {:6d} | {:6.2f} |".format(ID,mydict[ID][0],mydict[ID][1],mydict[ID][2],mydict[ID][3],mydict[ID][4],mydict[ID][5]))


#****************** maincode ***********************************************************
print_grades('test2.txt')
    
    
