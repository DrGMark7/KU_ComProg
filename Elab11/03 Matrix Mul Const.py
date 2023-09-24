def mul_const(A,c):
    new_matrix = []
    for row in A:
        n_row = []
        for j in row:
            n_row.append(j*c)
        new_matrix.append(n_row)

    return new_matrix

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2

print_matrix(mul_const(A,c))