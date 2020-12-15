################### Sample Solution ###################
def _product_of_two_vectors_sample_(a, b):
    l = []
    for i in range(len(a)) :
        l1=[]
        for k in range(len(b[0])):
            s = 0
            for j in range(0,len(a[0])) :
                s += a[i][j] * b[j][k]
            l1.append(s)
            #print("i:",i," k:",k,' j:',j,'\n',l1)
        l.append(l1) 
    return l
            



    
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(_product_of_two_vectors_sample_(a, b))
