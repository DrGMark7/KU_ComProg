x = []
while True:
    n = input("Enter a number (just [Enter] to quit): ")
    if n == "":
        break
    else:
        x.append(float(n))
if x == []:
    print("Nothing to do.")
else:
    print(f"Maximum value is {max(x):.2f}")
    print(f"Minimum value is {min(x):.2f}")
    print(f"Average value is {(sum(x)/len(x)):.2f}")