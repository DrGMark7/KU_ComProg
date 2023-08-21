p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

def simple_interest(p,r,t):
    return (p*(r/100)*t)+p

def compound_interest(p,r,t):
    return p*((1+(r/100))**t)

print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))