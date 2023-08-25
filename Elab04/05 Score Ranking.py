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
        print(f"Rank #{i+1}: {sorted(x,reverse=True)[i]}")