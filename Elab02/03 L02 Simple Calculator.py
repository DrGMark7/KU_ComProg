x = int(input("x: "))
Op = str(input("Operator: "))
y = int(input("y: "))
Op_list = ["+","-","*","/","%"]
if Op in Op_list:
    if Op == "+":
        print(x+y)
    elif Op == "-":
        print(x-y)
    elif Op == "*":
        print(x*y)
    elif Op == "/":
        print(f"{(x/y):.2f}")
    elif Op == "%":
        print(x%y) 
else:
    print("Unknown Operator")