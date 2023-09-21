def tri(n):
    if n == 1:
        return 'x'
    return tri(n-1)+'\n'+'x'*n

print(tri(8))