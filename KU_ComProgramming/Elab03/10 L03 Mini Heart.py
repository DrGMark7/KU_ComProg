import math
L = float(input("Please enter the value of L: "))
def MiniHeart(x):
    return x**2+(math.pi*((x/2)**2))
print(f"Area is {MiniHeart(L):.4f}")