def remaining_loan_balance (principal, annual_interest_rate, duration , number_of_payments) :
    r = annual_interest_rate / 1200
    n = duration * 12
    p = number_of_payments
    if r != 0 :
        y = (principal*(((1+r)**n)-((1+r)**p))) / (((1+r)**n)-1)
    else :
        y = principal*(1-(p/n))
    return y
