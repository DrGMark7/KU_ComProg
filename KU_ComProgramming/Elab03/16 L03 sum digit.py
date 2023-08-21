n   = int(input('Enter a number (0 to 9999): '))

def digit(n):
    return int(str(n)[-1])

def tens(n):
    if len(str(n)) >= 2:
        return int(str(n)[-2])
    else:
        return 0
def hundreds(n):
    if len(str(n)) >= 3:
        return int(str(n)[-3])
    else:
        return 0

def thousands(n):
    if len(str(n)) >= 4:
            return int(str(n)[-4])
    else:
            return 0

def sum_digits(n):
    return digit(n)+tens(n)+hundreds(n)+thousands(n)

print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))