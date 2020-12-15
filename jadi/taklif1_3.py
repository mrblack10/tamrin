#####################
def monthle_payment(principal, annual_interest_rate, duration):
    r = annual_interest_rate / 1200
    n = duration * 12
    if r != 0 :
        y = (principal * (r*((1+r)**n)))/(((1+r)**n)-1)
    else :
        y = principal / n
    return y

#####################

def remaining_loan_balance (principal, annual_interest_rate, duration , number_of_payments) :
    r = annual_interest_rate / 1200
    n = duration * 12
    p = number_of_payments
    if r != 0 :
        y = (principal*(((1+r)**n)-((1+r)**p))) / (((1+r)**n)-1)
    else :
        y = principal*(1-(p/n))
    return y

#### main program #########

principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

print ("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
print ("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(monthle_payment(principal, annual_interest_rate, duration)))
for x in range(1,duration+1):
    print ("YEAR:",x,"BALANCE:",int(remaining_loan_balance (principal, annual_interest_rate, duration , x*12)),"TOTAL PAYMENT",int(12*x*monthle_payment(principal, annual_interest_rate, duration)))
