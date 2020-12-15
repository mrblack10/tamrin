def calculate_grades(file_name):
    myfile = open(file_name, 'r')
    data = myfile.readlines()
    output = []
    for line in range(len(data)) :
        data[line] = data[line].strip().split(',')
    data = sorted(data,key = lambda index : index[0])
    #print(data)
    for line in range(len(data)) :
        for i in range(1,len(data[line])):
            data[line][i] = int(data[line][i])
        l = [data[line][0],sum(data[line][1:5])/4]
        #print(tuple(l))
        output.append(tuple(l))
    return tuple(output)




print(calculate_grades('azmon6_3.txt'))
