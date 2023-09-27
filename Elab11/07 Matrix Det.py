M = []
for i in range(3):
    M.append(list(map(int, input(f"Row {i+1} : ").split())))
a,b,c = M[0][0],M[0][1],M[0][2]
d,e,f = M[1][0],M[1][1],M[1][2]
g,h,i = M[2][0],M[2][1],M[2][2]
print(((a*e*i)+(b*f*g)+(c*d*h))-((g*e*c)+(h*f*a)+(i*d*b)))