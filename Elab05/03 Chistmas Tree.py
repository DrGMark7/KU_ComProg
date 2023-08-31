Levels = int(input("How many levels? "))
n = int(input("How big is each bush? "))
for _ in range(Levels):
    for i,j in zip(range(n-1,-1,-1),range(1,n*2,2)):
        print(i*" "+j*"*")