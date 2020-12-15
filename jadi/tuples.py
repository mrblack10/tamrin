#show some tuples ideas in functions

def jam_zarb (x,y):
    jam = x + y
    zarb = x * y
    return (jam,zarb)

(j,z) = jam_zarb(3,4)

s1 , s2 = jam_zarb(3,4)

t = jam_zarb(3,4)

print ("jam is",t[0],"and zarb is",t[1]) #or : print ("jam is",j,"and zarb is",z) #or : print ("jam is",s1,"and zarb is",s2)  

print(t)
