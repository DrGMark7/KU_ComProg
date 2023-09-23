def minus_matrix(A,B):
    new_matrix = []
    for row1,row2 in zip(A,B):
        row = []
        for i,j in zip(row1,row2):
            row.append(i-j)
        new_matrix.append(row)

    return new_matrix

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
print_matrix(minus_matrix(A,B))
