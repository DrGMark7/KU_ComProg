x = int(input("How many food you have : "))
l = []
for _ in range(x):
    k = []
    k.append(str(input("")).split())
    for i,j in zip(range(len(k[0])),k[0]):
        k[0][i] = int(j)
    l.append(k[0])
def plus(total,value):
    return total+value
def minus(total,value):
    return total-value

l_plus,l_minus = [],[]
for i in l:
    if i[-1] == 1:
        l_plus.append(i[0])
    else:
        l_minus.append(-1*i[0])
if (sum(l_plus)-sum(l_minus)) > 0:
    print(plus(sum(l_plus),sum(l_minus)))
else:
    print(minus(sum(l_plus),sum(l_minus)))

