n = input()
n = int(n)
x = 1
a = 1
while (x>0):
    ######
    for i in range(1,x+1):
        print("*",end ='')
    x = x + a
    print("")
    ######   or -> print("*" * x)
    if x == n:
        a = -1
    
