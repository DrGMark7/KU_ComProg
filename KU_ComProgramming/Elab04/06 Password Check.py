count = 1
while True:
    n = input("Enter the password: ")
    if n == "I love Python":
        print("Correct password")
        print("Access granted")
        break
    elif count < 3:
        print(f"Incorrect password, attempt #{count}")
        print("Access denied")
        count+=1
    else:
        print(f"Incorrect password, attempt #{count}")
        print("Access denied")
        print("Maximum attempts exceeded")
        break