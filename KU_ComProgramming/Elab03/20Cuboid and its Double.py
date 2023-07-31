w = float(input("Enter width: "))
l = float(input("Enter length: "))
h = float(input("Enter height: "))

def compute_rectangle_area(first_side, second_side):
    return first_side*second_side

def compute_surface_area(w,l,h):
    return 2*((compute_rectangle_area(w,l))+(l*h)+(h*w))

def compute_volume(w,l,h):
    return w*l*h

print(f"For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(w,l,h):.3f}")
print(f"Volume = {compute_volume(w,l,h):.3f}")
print("")
print("After doubling each side,")
print(f"For [{w*2:.2f} x {l*2:.2f} x {h*2:.2f}] cuboid: ")
print(f"Surface area = {compute_surface_area(w*2,l*2,h*2):.3f}")
print(f"Volume = {compute_volume(w*2,l*2,h*2):.3f}")
print("")