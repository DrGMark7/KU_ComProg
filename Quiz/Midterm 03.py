import calendar as c
m = int(input("Month : "))
y = int(input("Year : "))
day_name = ["Su","Mo","Tu","We","Th","Fr","Sa"]
month_name = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
def create_groups(input_list, group_size):
    result = []
    current_row = [0] * group_size
    current_index = 0
    
    for value in input_list:
        if current_index == 0:
            if current_row[0] != 0:
                current_row.pop(0)
                current_row.append(value)
                result.append(current_row)
                current_row = [0] * group_size
                current_index = 0
            
        current_row[current_index] = value
        current_index = (current_index + 1) % group_size
        
    result.append(current_row)
    return result

day_group = c.monthcalendar(y,m)
groups = create_groups(day_group, 7)[0]

print(" "*5+(month_name[m-1]+" "+str(y)))
print(' '.join(day_name))
try:
    for i in groups:
        for j in i:
            if j == 0:
                print("  ",end=" ")
            else:
                print("%2d" % j,end=" ")
        print()
except:
    pass