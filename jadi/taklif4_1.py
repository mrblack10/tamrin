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
            if "Test_" in data[line][i]:
                t[int(data[line][i][5])] = int(data[line][i+1])
        
        #print("dataline:",data[line])
        mydict[data[line][0]] = [data[line][1],t[1],t[2],t[3],t[4],sum(t)/4]
        #print(mydict[data[line][0]],"\n*****************")
    
    return mydict


print(create_grades_dict('test2.txt'))
