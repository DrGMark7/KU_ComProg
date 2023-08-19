H = int(input("How deep is the well? "))
U = int(input("How high the frog can jump up? "))
D = int(input("How far the frog slips down? "))

if (U == D) and (H != U):
    print("The frog will never escape from the well.")
    exit()
else:
    day = 0
    while H > 0:
        day = day + 1
        H = H-U
        if H > 0:
            print(f"On day {day} the frog leaps to the depth of {H} meters.")
            H = H+D
            print(f"At night he slips down to the depth of {H} meters.")
    print(f"The frog gets out of the well on day {day}.")

    
    
