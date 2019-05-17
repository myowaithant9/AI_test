principal = float(input("Loan > "))
interest_rate = float(input("Annual interest rate(%) > "))
repay_amt = int(input("Repayment amount > "))

counter = 0
total_interest = 0
total_payment = principal
tmp = ""

def interest_cal(principal, interest_rate):
    interest_amt = ( ( principal / 100 ) * interest_rate )/12
    return interest_amt

def balance_cal(principal, repay_amt, interest_amt):
    remaining_bal = (principal - repay_amt) + interest_amt
    return remaining_bal

def counter_cal(counter):
    if (counter < 12) :
        tmp = str(counter) + "th month"
        if (counter == 1) : tmp = str(counter) + "st month"
        if (counter == 2) : tmp = str(counter) + "nd month"
        if (counter == 3) : tmp = str(counter) + "rd month"
    else:
        year = int(counter / 12)
        month = counter % 12
        tmp = str(year) + " Year and " + str(month) + "th month"
        if (month == 0): tmp = str(year) + " Year"
        if (month == 1): tmp = str(year) + " Year and " + str(month) + "st month"
        if (month == 2): tmp = str(year) + " Year and " + str(month) + "nd month"
        if (month == 3): tmp = str(year) + " Year and " + str(month) + "rd month"
    return tmp

while (principal > repay_amt):
    counter += 1
    tmp = counter_cal(counter)
    
    interest_amt = interest_cal(principal, interest_rate)
    remain_bal = balance_cal(principal, repay_amt, interest_amt)
    total_payment += interest_amt

    print(str(tmp) + ": Repayment amount " + str(repay_amt) + " Ks remaining " + str(int(remain_bal)) + " Ks")
    principal = remain_bal

else :
    counter += 1
    tmp = counter_cal(counter)
    interest_amt = interest_cal(principal, interest_rate)
    repay_amt = principal + interest_amt
    total_payment += interest_amt
    print(str(tmp) + ": Repayment amount " + str(int(repay_amt)) + " Ks pay off. " + "Total repayment:  " + str(int(total_payment)) + " Ks")