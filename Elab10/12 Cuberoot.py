def newton_cuberoot(x,y):
    if abs(x**3 - y) <= 10e-6:
        return x
    new_x = ((y/x**2)+2*x)/3
    return newton_cuberoot(new_x,y)

def cuberoot(y):
    return newton_cuberoot(1.0, y)

print(cuberoot(27))