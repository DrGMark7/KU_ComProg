a = int(input("Enter your age: "))
x = float(input("Enter your net income: "))
if a in range(15,61):
    if x >= 1 and x <= 30000:
        b = x*0.2
        print(f"Your negative income tax is {b:.2f} Baht.")
    elif x > 30000 and x < 80000:
        b = (30000*0.2) - (x-30000)*0.12
        print(f"Your negative income tax is {b:.2f} Baht.")
    else:
        print("Invalid income.") 
elif x < 1:
    print("Invalid income.")
else:
    print("Invalid age.")