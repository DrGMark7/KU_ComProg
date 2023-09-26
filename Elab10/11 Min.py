def Min(lst, n):
    lst = lst[:n]
    lst.remove(max(lst))
    if len(lst) == 1:
        return lst[0]
    else:
        return Min(lst,n)
    

lst = [3, 8, 2, 9, 7, 1, 5]
print(Min(lst,4))
