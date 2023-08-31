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

def printAllPrimes(limit):
    number_list,Bucket_list = range(limit+1),[]
    for i in number_list:
        if isPrime(i) == True:
            Bucket_list.append(str(i))
    print(' '.join(Bucket_list))