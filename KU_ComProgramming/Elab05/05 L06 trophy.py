n = int(input("input: "))
a = n//2
for i,j in zip(range((a),-1,-1),range(1,a*2,2)):
    print(i*" "+j*"#")
print("#"*n)
for i,j in zip(range(1,a+1,1),range(a*2-1,-2,-2)):
    print((" "*(i))+j*"#")