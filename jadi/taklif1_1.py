def monthle_payment(principal, annual_interest_rate, duration):
    r = annual_interest_rate / 1200
    n = duration * 12
    if r != 0 :
        y = (principal * (r*((1+r)**n)))/(((1+r)**n)-1)
    else :
        y = principal / n
    return y
