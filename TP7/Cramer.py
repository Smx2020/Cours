from Gauss import *

def Resolution(A,B):
    M = copy(A)
    for i in range(len(M)):
        M[i].append(B[i])
    B = Reduite_max(M)
    temp = []
    for i in range(len(B)):
        temp.append(B[i][-1])
    return(temp)

def Inverse(A):
    B = "a"
