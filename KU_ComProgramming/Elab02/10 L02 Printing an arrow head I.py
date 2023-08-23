while True:
    n = int(input("Input number: "))
    if n%2 == 1:
        for i in range(1,n+1):
            print(i*"x")
        for i in range(n-1,0,-1):
            print(i*"x")
        break
    else:
        print("Please input odd number")