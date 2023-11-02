def check_prime(n):
    divided_number = []
    for i in range(1,n):
        if n % i == 0:
            divided_number.append(i)

    if n == 1:
        return False
    elif len(divided_number) == 1:
        return True
    else:
        return False
    
for i in range(1,20):
    if check_prime(i):
        print(f"{i} is Prime")
    else:
        print(f"{i} is not prime")