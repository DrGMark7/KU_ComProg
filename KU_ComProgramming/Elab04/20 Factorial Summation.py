def factorial(x):
    n,Ln = 1,[]
    for i in range(1,x+1):
        n*=i
        Ln.append(n)
    return Ln

k = int(input("Input k: "))
for i,j in zip(range(1,k+1),factorial(k)):
    print(f"{i}! = {j}")
print(f"Summation of factorial 1!-{k}! = {sum(factorial(k))}")
