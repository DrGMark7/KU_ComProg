def isPrime(number):
    if number == 1:
        return False
    elif number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                return False
                break
        else:
            return True
        
def list_factors(n):
    list_f = []
    for i in range(1,n+1):
        if n % i == 0 :
            list_f.append(i)
    return list_f

def find_sum_and_num_factors(n):
    SUM,NUM = sum(list_factors(n)),len(list_factors(n))
    return (SUM,NUM)
num = int(input("Enter positive number: "))
print(f"Factors of {num} are")
List_to_str = ' '.join(str(e) for e in list_factors(num))
print(List_to_str)
print(f"Sum of {List_to_str} is {find_sum_and_num_factors(num)[0]}")
print(f"Number of factors is {find_sum_and_num_factors(num)[1]}")
if isPrime(num) == True:
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")