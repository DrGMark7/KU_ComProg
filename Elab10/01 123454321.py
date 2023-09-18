def printit(m, n):
    if m == n:
        return str(n)
    return str(m) + printit(m+1,n) + str(m)

print(printit(8,11))
