def power_matrix(A,c):
    new_matrix = []
    def mul_matrix(A,B=A):
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
    
    for _ in range(c-1):
        A = mul_matrix(A)
        new_matrix = A
    return new_matrix

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
        
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
print_matrix(power_matrix(A,c))