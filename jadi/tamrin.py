def y(n,x):
	fac=1
	for i in range(2,n+3):
		fac *= i
	#print(fac)
	y = (x**(n+1))/fac
	return y
t = True
i = 0
Y = 1
j = 1
while(j>0.0005):
    j = y(i,0.01)
    print("i:",i,"{:.4f}".format(j))
    i+=1
    Y += float("{:.4f}".format(j))
print("Y:{:.4f}".format(Y))
"""
sasalaacdaasllsa
"""
#print(a)

