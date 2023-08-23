a = []
for i in range(1,int(input("How many day : "))+1):
    a.append(float(input(f"Input price in day {i} : "))*(0.96-(i/100)))
print(f"Summary price = {sum(a):.2f}")