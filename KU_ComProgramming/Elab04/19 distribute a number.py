def get_distribution(number):
    text = []
    for i,j in zip(range(len(str(number))),list(str(number))[::-1]):
        text.append(f"{j}x10^{i}")
    return " + ".join(text)

def count_digits(number):
    number = abs(number)
    count = 0
    if number == 0:
        return 1
    while number != 0:
        number //= 10
        count += 1
    return count

def get_last_digit(number):
    return int(str(number)[-1])

N = int(input("Input number: "))
print(f"{N} = {get_distribution(N)}")
print(f"{N} = {count_digits(N)}")
print(f"{N} = {get_last_digit(N)}")