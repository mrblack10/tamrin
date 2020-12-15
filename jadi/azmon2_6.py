n=input()
n = int(n)
d = n//86400
n = n%86400
h = n//3600
n = n%3600
m = n//60
n = n%60
s = n
print(d,'days',h,'hours',m,'minutes',s,'seconds')
    
