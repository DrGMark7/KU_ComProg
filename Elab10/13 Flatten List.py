def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            result.extend(flatten_list(item))
    return set(result)

# Test the function

print(flatten_list([1, 2, [[2], [3, 4], 5], 4, [3], [[4]]]))