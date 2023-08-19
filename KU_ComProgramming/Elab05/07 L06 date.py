d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

def isleapyear(year):
    if year >= 1:
        if (year % 400 == 0) and (year % 100 == 0):
            return True
        elif (year % 4 ==0) and (year % 100 != 0):
            return True
        else:
            return False
    else:
        return False

count = 0 
day_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
day_not_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
if isleapyear(y) == False:
    count += d
    if m > 1:
        for i in range(0,m-1):
            count += day_not_leap[i]
else:
    count += d
    if m > 1:
        for i in range(0,m-1):
            count += day_leap[i]
print(count) 