Police_D,Criminal_D,n = 0,100,1
while True:
    D = int(input("Input distance: "))
    Police_D += D
    print(f"Police distance: {Police_D}")
    Criminal_D += 2**(n)
    print(f"Criminal distance: {Criminal_D}")
    if Police_D >= Criminal_D:
        print("Caught him!")
        break
    n += 1