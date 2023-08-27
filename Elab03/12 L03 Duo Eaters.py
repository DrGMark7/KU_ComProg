S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
n = int(input("Input Gane's eating rate (n): "))

def eat(S,P,n):
    a = S//P
    b = (S-(a*P))//n
    c = S-(a*P)-(b*n)
    return (a,b,c)
    

print(f"Paun eats {eat(S,P,n)[0]} time(s)")
print(f"Gane eats {eat(S,P,n)[1]} time(s)")
print(f"Remaining {eat(S,P,n)[2]} for dog")