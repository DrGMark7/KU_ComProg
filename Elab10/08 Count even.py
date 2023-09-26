def count_even(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 0:
        return 1 + count_even(lst[1:])
    else:
        return 0 + count_even(lst[1:])