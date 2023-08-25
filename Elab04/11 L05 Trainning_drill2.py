def fibo(n):
    n1,n2,count  = 0,1,0
    x = []
    if n+1 == 1:
       x.append(1)
    else:
       while count < n+1:
            x.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return x
n = int(input("Day: "))
print(' '.join(map(str,fibo(n)[1:])))