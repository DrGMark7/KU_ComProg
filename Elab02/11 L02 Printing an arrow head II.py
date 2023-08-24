t = str(input("Enter a string: "))
x = int(input("Enter arrow's size (greater than 0): "))
if x > 0:
    for i in range(1,(x//2)+1,1):
        print(" "*(i-1)+t)
    if x%2 == 1:
        print(" "*(x//2)+t)
    for i in range((x//2),0,-1):
        print(" "*(i-1)+t)
else:
    print("Size must be greater than 0.")