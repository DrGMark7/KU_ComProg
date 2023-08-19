t = input("Enter a string: ")
for i,j in zip(t,range(len(t))):
    print(j*' '+i)
