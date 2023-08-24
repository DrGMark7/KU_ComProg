U = str(input("Username: "))
P = str(input("Password: "))
if U == ADMIN_USERNAME and P == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")