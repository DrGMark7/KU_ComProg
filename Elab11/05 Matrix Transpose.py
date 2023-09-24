def transpose_matrix(A):
    new_matrix = []
    for i in range(len(A[0])):
        new_row =[]
        for row in A:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2],[3,4],[5,6]]
print_matrix(transpose_matrix(A))