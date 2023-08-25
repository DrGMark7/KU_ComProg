x = []
while True:
    n = float(input("Enter a number (or just zero to exit): "))
    if n == 0:
        x.append(n)
        break
    else:
        x.append(n)
pos_nos = list(filter(lambda x: (x > 0), x))
minus_nos = list(filter(lambda x: (x < 0), x))
zero_nos = list(filter(lambda x: (x == 0), x))
if (pos_nos and minus_nos) == None:
    print(f"Sum of positive numbers is {0:.2f}")
    print(f"Sum of negative numbers is {0:.2f}")
elif (pos_nos == None):
    print(f"Sum of positive numbers is {0:.2f}")
    print(f"Sum of negative numbers is {sum(minus_nos):.2f}")
elif (minus_nos == None):
    print(f"Sum of positive numbers is {sum(pos_nos):.2f}")
    print(f"Sum of negative numbers is {0:.2f}")
else:
    print(f"Sum of positive numbers is {sum(pos_nos):.2f}")
    print(f"Sum of negative numbers is {sum(minus_nos):.2f}")
