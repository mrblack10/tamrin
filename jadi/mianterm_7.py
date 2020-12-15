def pattern_sum(a, b):
    s = 0
    st = ''
    for i in range(1,b+1) :
        st += str(a)
        s+= int(st)
        #print(st,s)
    return s

print(pattern_sum(5, 3))
