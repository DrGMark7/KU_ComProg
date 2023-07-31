Gold = float(input("Input Gold: "))

def draw_hammer(N):
    print(" "+"o"*(3*N+4)+" ")
    for _ in range(2*N+1):
        print("o"*(3*N+6))
    print(" "+"o"*(3*N+4)+" ")
    for _ in range(N+2):
        print(" "*(N+3)+"o"*(N))
    for _ in range(N):
        print(" "*(N+2)+"o"*(N+2))
    print(" "*(N+3)+"o"*N)

if 1000 <= Gold < 2000:
    draw_hammer(1)
elif 2000 <= Gold < 3000:
    draw_hammer(2)
elif 3000 <= Gold < 4000:
    draw_hammer(3)
elif 4000 <= Gold < 5000:
    draw_hammer(4)
else:
    print("Not enough gold.")