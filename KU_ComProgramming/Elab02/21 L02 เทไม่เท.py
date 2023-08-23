m = int(input("Minutes before due: "))
t = float(input("Temperature: "))
a = str(input("Is it raining (y/n)? ")).lower()
d = round(m/(1440))
if d == 0:
    d = 1
print(f">>> {d} days before due.")
if d < 2:
    print(">>> I will do the assignment.")
elif d > 5:
    print('>>> I will not do the assignment.')
elif t > 40 or (t > 25 and a=="y"):
    print(">>> I will not do the assignment.")
else:
    print(">>> I will do the assignment.")