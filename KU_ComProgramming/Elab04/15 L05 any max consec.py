x = []
while True:
    n = int(input(""))
    if n == 0:
        x.append(n)
        break
    else:
        x.append(n)

def find_most_adjacent_same_number(lst):
    if not lst:
        return None, 0

    max_count = 1
    current_count = 1
    current_number = lst[0]
    most_adjacent_number = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_count += 1
        else:
            current_count = 1
            current_number = lst[i]

        if current_count > max_count:
            max_count = current_count
            most_adjacent_number = current_number

    return [most_adjacent_number, max_count]

print(find_most_adjacent_same_number(x)[1])
print(find_most_adjacent_same_number(x)[0])



