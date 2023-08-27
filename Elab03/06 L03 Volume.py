import math

def find_cylinder_volume(h,r):
    return math.pi*(r**2)*h


r = float(input("radius = "))
h = float(input("height = "))
V = find_cylinder_volume(h,r)

print("Volume = %.2f" %V)