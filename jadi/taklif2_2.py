def single_insert_or_delete (s1,s2) :
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2 :
        return 0
    smax = max(s1,s2,key = lambda item : len(item))
    smin = min(s1,s2,key = lambda item : len(item))
    #print ("smax:",smax,'\nsmin:',smin)

    if (len(smax)-len(smin))==1 :
        t=0
        for i in range(0,len(smin)) :
            if smax[i] == smin[t] :
                t = t+1
        if (len(smin)-t)<2 :
            return 1
        else :
            return 2
    else:
        return 2

s1 = input("s1:")
s2 = input("s2:")

print(single_insert_or_delete (s1,s2))
