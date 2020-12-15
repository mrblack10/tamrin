def FB (n):
    c = 1
    a,b = 0,1
    while c <= n:
        a,b = b,a+b
        c+=1
        yield b

# for num in FB(100):
#     print(num)

l = [num for num in range(10)]
print(l)