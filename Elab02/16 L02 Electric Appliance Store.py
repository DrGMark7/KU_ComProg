TV = int(input("How many TVs? "))
DVD = int(input("How many DVD players? "))
AUD = int(input("How many Audio Systems? "))
p = TV*6000 + DVD*1500 + AUD*3000
print(f"Total price is {p:.2f} baht.")
if p >= 24000:
    print(f"You've got a discount of {p*0.2:.2f} baht.")  
    print(f"Your payment is {p*0.8:.2f} baht. Thank you!")
else:
    print(f"Your payment is {p:.2f} baht. Thank you!")
    pass  
