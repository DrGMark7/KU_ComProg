x = float(input("Enter buying amount: "))
if x >= 1000 and x <3000:
    print(f"Amount due after discount is {x*0.9 :.2f} baht.")
elif x >= 3000:
    print(f"Amount due after discount is {x*0.85 :.2f} baht.")
else:
    print(f"Amount due after discount is {x*1.00 :.2f} baht.")