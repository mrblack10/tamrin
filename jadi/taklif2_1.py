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
    else :
        return 2

    
s_1 = input("s1:")
s_2 = input("s2:")

print (find_mismatch (s_1 , s_2))
