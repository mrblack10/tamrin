def kamel(x):
    s = 0
    for i in range(1,x-1):
        if (x % i)==0:
            s = s + i
    if s==x :
        return True
    else:
        return False
  
    
