n = int(input())
print("."*n)

for i,j in zip(range((n-4),0,-2),range(0,(int((n-3)/2)),1)):
    print("."+" "*j+"."+" "*i+"."+" "*j+".")

print("."+" "*int((n-3)/2)+"."+" "*int((n-3)/2)+".")

for i,j in zip(range(1,(n-4)+1,2),range((int((n-3)/2))-1,-1,-1)):
    print("."+" "*j+"."+" "*i+"."+" "*j+".")

print("."*n)