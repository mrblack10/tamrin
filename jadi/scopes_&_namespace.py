# show scopes

def myfun():
    def innerfun():
        print("i am in inner function and x is",x)
    x = 4
    innerfun()
    print('i am in function and x is',x)

x = 5
print("i am in global and x is",x)
myfun()
print("i am in global and x is",x)


local



