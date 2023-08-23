target = 72

while True:
    x = float(input("Enter your guess (0 - 100): "))
    if x in range(0,101,1):
        if x == target:
            print("Congratulations, your guess is correct.")
            break
        elif x > target:
            print("Sorry, your guess is too high, try again later.")
        elif x < target:
            print("Sorry, your guess is too low, try again later.")
    else:
        print("Sorry, out of range, try again later.")