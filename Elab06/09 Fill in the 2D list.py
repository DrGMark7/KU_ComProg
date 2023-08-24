n = int(input("Enter the number of rows or columns : "))
List = []
for i in range(n):
    for j in range(1,n+1):
        print("%2d" % (i+j), end=" ")
    print()