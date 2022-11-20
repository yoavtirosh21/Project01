def futureValue(p, r, m, t):
    # p  principal, the amount deposited
    # r  annual rate of interest in decimal form
    # HELLO
    # m  number of times interest is compounded per year
    # t  number of years
    i = r   # interest rate per period
    n = m * t   # total number of times interest is compounded
    amount =  p * ((1 + i) ** n)
    
    print(f"{'Principal' : <20}{'Annual Rate' : ^20}{'Compound #' : ^15}{'Year #' : ^15}{'Balance' : <20}")
    print(f"{'${0:,.2f}'.format(p) : <20}{'{0:,.2f}'.format(r) : ^20}{'{0:,.0f}'.format(m) : ^15}{'{0:,.0f}'.format(t) : ^15}{amount : <20}")
    return amount

## Find the future value for a saving account deposit
p = eval(input("Enter amount deposited: "))
r = eval(input("Enter annual rate of interest in decimal form: "))
m = eval(input("Enter number of times intrest is compounded per year: "))
t = int(input("Enter number of years: "))
balance = futureValue(p, r, m, t)

