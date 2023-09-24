def mul_matrix(A,B):
    new_matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            value = []
            for a,b in zip(A[i],[row[j] for row in B]):
                value.append(a*b)
            row.append(sum(value))
        new_matrix.append(row)
    return new_matrix

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(mul_matrix(A,B))