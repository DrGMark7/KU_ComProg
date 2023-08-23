t = input("Enter your buffet choice: ")
if t in ['Japanese','Korean']:
    a = input("Is today Wednesday (yes/no)? ")
    if t == 'Japanese':
        if a == "yes":
            print(f"Your payment is {1000*0.85:.2f} Baht.")
        else:
            print(f"Your payment is {1000:.2f} Baht.")
    else:
        if a == "yes":
            print(f"Your payment is {1500*0.85:.2f} Baht.")
        else:
            print(f"Your payment is {1500:.2f} Baht.")
else:
    print(f"Sorry, there is no {t} buffet.")   