def aval(n):
    if n==0 or n==1:
        return False
    for x in range(2,n-1):
        if (n % x)==0:
            return False
    return True
#print (aval(1))

