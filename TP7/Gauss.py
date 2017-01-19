def pivot(A,j):
    "cherche le premier pivot"
    for i in range(j,len(A)):
        if A[i][j] != 0:
            return(i)

def pivot_max(A,j):
    "cherche le plus grand pivot"
    i0 = j
    for i in range(j,len(A)):
        if abs(A[i][j]) > abs(A[i0][j]):
            i0 = i
    return(i0)
