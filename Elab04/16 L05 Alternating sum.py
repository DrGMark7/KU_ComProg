def Alternative_sum(n):
    l1 = sum(list(range(1,n+1))[::2])
    l2 = sum(list(range(1,n+1))[1::2])
    return l1-l2

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,Alternative_sum(n)))