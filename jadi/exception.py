# Error handling
#****************EX_1**********************
number = input ("give me a number:")

try:
    number = float(number)
except ValueError:
    number = 0
    print("bad number. I will assume 0")

print(number+7)

#****************EX_2**********************
try:
    fp = open('test2.txt','r')
except FileNotFoundError:
    print("can not open this file!")
else:
    data = fp.read()
    print(data)
    fp.close()
finally:
    print("done")

#****************EX_3**********************
mynumber= input("give me a number:")
try :
    mynumber = float(mynumber)
    print(10/mynumber)
except ValueError:
    print("ValueError!")
except ZeroDivisionError:
    print("oh... a zero!")
finally:
    print("done")
    
