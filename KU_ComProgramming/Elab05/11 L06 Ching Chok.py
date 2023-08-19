x = int(input("Enter lucky number : "))
n = int(input("Enter amount of candidates : "))
List,Count = [],[]
for i in range(n):
    List.append(str(input(f"Enter ID card number {i+1}: ")))

for i in List:
    Count.append([i.count(str(x)),int(i)])
print(f"Winner: {sorted(Count,reverse=True)[0][1]}")