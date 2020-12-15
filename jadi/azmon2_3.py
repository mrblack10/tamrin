age=input("Type your age:")
age = int(age)
if age <= 0 :
    print('UNBORN')
elif age >0 and age<=150 :
    print('ALIVE')
else:
    print('VAMPIRE')
