# a program to calculate the square root

def jazr(number):
    guess = number/2

    error =0.01

    iteration = 0

    while (abs(number - guess**2) > error):
        iteration = iteration + 1
        #print ("-> on iteration",iteration," my guess is",guess)
        taqsim = number / guess
        guess = (taqsim + guess) / 2
    print ("the square root of",number,"is:",guess)

x = input("give me n,I will give you the radical(n):")

jazr(float(x))

jazr(50)
jazr(100)


    
