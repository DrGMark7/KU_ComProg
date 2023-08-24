def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

array = [int(input()),int(input()),int(input())]
a = bubble_sort(array)
print(f"{a[0]} {a[1]} {a[2]}")