def	echange_ligne(A,i1,i2):
	"echange les lignes i1 et i2 de A"
	for j in range(len(A[0])):
		c = A[i1][j]
		A[i1][j] = A[i2][j]
		A[i2][j] = c
	return(A)

def	echange_ligne_c(A,i1,i2):
	"Cree une nouvelle matrice en echangeant les lignes i1 et i2 de A"
	out = []
	for i in range(len(A)):
		temp = []
		for j in range(len(A[0])):
			temp.append(A[i][j])
		out.append(temp)
	return(echange_ligne(out,i1,i2))

def	multiplier_ligne(A,i,l):
	"Multiplie les coeffs de la ligne i par l"
	for j in range(len(A[i])):
		A[i][j] = A[i][j] * l
	return(A)

def	multiplier_ligne_c(A,I,l):
	"Cree une nouvelle matrice et fais multiplier ligne"
	out = []
	for i in range(len(A)):
		temp = []
		for j in range(len(A[0])):
			temp.append(A[i][j])
			out.append(temp)
			return(multiplier_ligne(A,I,l))

def addition_ligne(A,i1,i2):
	"Additionne la ligne i1 et i2"
	for j in range(len(A[0])):
		A[i1][j] = A[i1][j] + A[i2][j]
	return(A)

def addition_ligne_c(A,i1,i2):
	"Cree une nouvelle matrice et fais addition_ligne"
	out = []
	for i in range(len(A)):
		temp = []
		for j in range(len(A[0])):
			temp.append(A[i][j])
		out.append(temp)
	return(addition_ligne(out,i1,i2))

def addition_multiple_ligne(A,i1,i2,l):
	"Additionne et multiplie la ligne i2 a i2"
	for j in range(len(A[0])):
		A[i1][j] = A[i1][j] + l * A[i2][j]
	return(A)

def addition_multiple_ligne_c(A,i1,i2,l):
	"Cree une nouvelle matrice et fais addition_ligne"
	out = []
	for i in range(len(A)):
		temp = []
		for j in range(len(A[0])):
			temp.append(A[i][j])
		out.append(temp)
	return(addition_multiple_ligne(out,i1,i2,l))

######################  Exercice Gauss  ######################################

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

def Gauss(A):
    for i in range(len(A)):
        k = pivot(A,i)
        if i != k:
            echange_ligne(A,i,k)
        
