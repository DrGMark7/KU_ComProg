def divnums(n,d):
    if n==d:
        return str(n)+" "
    
    elif n%d == 0:
        return divnums(n-1,d)+str(n)+" "
    
    return divnums(n-1,d)

print(divnums(10,3))