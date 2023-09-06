row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))

Array = []
print("-----------------")
for i in range(8):
    Col = []
    for j in range(8):
        if i == row and j == col:
            Col.append('R')
        elif i == row or j == col:
            Col.append('x')
        else:
            Col.append(' ')
    Array.append(Col)

for i in Array:
    print('|'+'|'.join(i)+'|')
    print("-----------------")