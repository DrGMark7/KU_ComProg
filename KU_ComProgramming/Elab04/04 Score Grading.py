import statistics as s

def sd(x):
    M,a= round(s.mean(x),3),0
    for i in x:
        a = a+(i-M)**2
    return (a/(len(x)-1))**0.5 

def grade(n,x):
    sd = SD
    if n >= (m+1.5*sd):
        V = "A"
    elif (m+1*sd <= n < m+1.5*sd ):
        V = "B+"
    elif (m+0.5*sd <= n < m+1*sd ):
        V = "B"
    elif (m <= n < m+0.5*sd):
        V = "C+"
    elif (m-0.5*sd <= n < m):
        V = "C"
    elif (m-1*sd <= n < m-0.5*sd):
        V = "D+"
    elif (m-1.5*sd <= n < m-1*sd):
        V = "D"
    elif n < m-0.5*sd :
        V = "F"
    else:
        return "Wrong number"
    return V

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
    m,SD = s.mean(x),sd(x)
    print(f"Average score is {m:.2f}")
    print(f"Standard deviation is {SD:.2f}")

    for i in range(len(x)):
        print(f"Score #{i+1}: {(x)[i]} grade: {grade(x[i],x)}")