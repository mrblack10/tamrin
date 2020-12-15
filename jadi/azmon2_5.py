n=input()
n = int(n)

if n<0 or n>168 :
    print('INVALID')
elif n<=41 :
    print('YOU MADE',n*8,'DOLLARS THIS WEEK')
elif n<=50 :
    print('YOU MADE',(40*8)+(n-40)*9,'DOLLARS THIS WEEK')
else:
    print('YOU MADE',(40*8)+(10*9)+(n-50)*10,'DOLLARS THIS WEEK')
    
