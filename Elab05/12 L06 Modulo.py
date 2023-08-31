N = int(input("N: ")) 
M = int(input("M: "))
Number = []
for i in range(1,N+1):
    Number.append(int(input(f"Input number {i}: ")) % M)
print(len(set(Number)))
