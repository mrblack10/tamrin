def spelling_corrector(s1,s2):
    s1 = s1.lower().split()
    #print ("s1:",s1,"\ns2:",s2,'type:',type(s2))
    output = ''
    def find_mismatch (s_1 , s_2) :
        s_1 = s_1.lower()
        s_2 = s_2.lower()
        
        if s_1 == s_2 :
            return 0
        elif len(s_1) == len(s_2) :
            t = 0
            for i in range(0,len(s_1)) :
                if  s_1[i] != s_2[i] :
                    t = t + 1
            if t == 1 :
                return 1
            else :
                return 2

    def single_insert_or_delete(s1,s2):
        s1=s1.lower()
        s2=s2.lower()
        if s1==s2:
            return 0
        if abs(len(s1)-len(s2))!=1:
            return 2

        if len(s1)>len(s2):
            
            for k in range(len(s2)):
                if s1[k]!=s2[k]:
                    if s1[k+1:]==s2[k:]:
                        return 1
                    else:
                        return 2
            return 1
        else: 
            for k in range(len(s1)):
                if s1[k]!=s2[k]:
                    if s1[k:]==s2[k+1:]:
                        return 1
                    else:
                        return 2
            return 1
            
    for i in s1 :
        t = True
        #print ("i:",i)
        for j in s2 :
            if len(i) < 3 :
                break
            #print("  j:",j,end="    ")
            if find_mismatch (i,j) == 1 or single_insert_or_delete (i,j) == 1 :
                output = output + j
                t = False
                break
        if t==True :
            output = output + i
        if i != s1[len(s1)-1]:
            output = output + ' '
        #print("\noutput--->",output,"\n ***********")
    return output.lower()

s1 = "Wee lpve Pythen"
s2 = ['we', 'Live', 'In', 'Python']

print(spelling_corrector(s1,s2))
            
