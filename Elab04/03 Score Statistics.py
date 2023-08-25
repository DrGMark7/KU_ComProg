x = []
while True:
    n = input("Enter student score (or just ENTER to end): ")
    if n == "":
        break
    else:
        x.append(int(n))
if x == []:
    print("Nothing to do.")
else:
    for i in range(len(x)):
        print(f"Score #{i+1}: {(x)[i]}")
    print(f"Average score is {(sum(x)/len(x)):.2f}")
    print(f"Minimum score is {min(x)}")
    print(f"Maximum score is {max(x)}")