def plus_matrix(A,B):
    new_matrix = []
    for row1,row2 in zip(A,B):
        row = []
        for i,j in zip(row1,row2):
            row.append(i+j)
        new_matrix.append(row)

    return new_matrix

def minus_matrix(A,B):
    new_matrix = []
    for row1,row2 in zip(A,B):
        row = []
        for i,j in zip(row1,row2):
            row.append(i-j)
        new_matrix.append(row)

    return new_matrix

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

def transpose_matrix(A):
    new_matrix = []
    for i in range(len(A[0])):
        new_row =[]
        for row in A:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix

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

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2
GOD_MATRIX = mul_matrix(plus_matrix(A,transpose_matrix(B)),minus_matrix(power_matrix(C,c),D))
print_matrix(GOD_MATRIX)