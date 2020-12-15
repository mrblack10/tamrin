def ke_mim_mim (a,b) :
    be_mim_mim = min(a,b)
    while (be_mim_mim > 1):
        if ((a % be_mim_mim) == 0)and((b % be_mim_mim) == 0):
            break 
        be_mim_mim = be_mim_mim-1
    y = (a*b)/be_mim_mim
    return int(y)

#x = int(input("x:"))
#y = int(input("y:"))

#print(ke_mim_mim(x,y))
