def power(n,k):
    if k == 0:
        return 1
    else:
        return n*power(n,k-1)
    
print(power(2,9))