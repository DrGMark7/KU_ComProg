def in_list(lst,x):
    if len(lst) == 0:
        return False
    if lst[0] == x:
        return True
    else:
        return in_list(lst[1:],x)