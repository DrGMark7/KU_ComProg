import math

def area_of_circle(k):
    return math.pi*((k/2)**2)

d = input("Diameter: ")
d_float = float(d)

area = area_of_circle(d_float)
print(f"area = {area:.3f}")
