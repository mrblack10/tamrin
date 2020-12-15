def my_final_grade_calculation(filename):
    fp = open(filename,'r')
    data = fp.readlines()
    fp.close()
    #print(data,end = '\n*********************\n')
    my_dict = {}
    for line in range(len(data)):
        data[line] = data[line].strip().split(',')
        for i in range(1,len(data[line])):
            data[line][i] = int(data[line][i])
            
        data[line].remove(min(data[line][1:6]))
        data[line].remove(min(data[line][1:5]))
        data[line].remove(min(data[line][5:9]))
        point = (sum(data[line][1:5])/4*(25/100)) + (sum(data[line][5:8])/3*(25/100)) + (data[line][8]*(25/100)) + (data[line][9]*(25/100))
        if point >= 60 :
            my_dict[data[line][0].lower()] = "pass"
        else :
            my_dict[data[line][0].lower()] = "fail"
            
        #print("line:",line+1," ---->",data[line])
    return my_dict 




print(my_final_grade_calculation('payanterm_4.txt'))
