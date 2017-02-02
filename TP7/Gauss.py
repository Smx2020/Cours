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

def copy(A):
    a_c = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])):
            temp.append(A[i][j])
        a_c.append(temp)
    return(a_c)

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

def Gauss_max(A):
	a_c = copy(A)
	for i in range(len(a_c)):
		k = pivot_max(a_c,i)
		if i != k:
			echange_ligne(a_c,i,k)	#Met la ligne avec le pivot en haut
		coeff = a_c[i][i]
		for j in range(i + 1,len(a_c)):
			addition_multiple_ligne(a_c,j,i,-1 * a_c[j][i] / coeff )	#Calcul les lignes
	return(a_c)

def Gauss_un_max(A):
	B = Gauss_max(A)
	for i in range(len(B)):
		multiplier_ligne(B,i,1/(B[i][i]))	#Multiplie les lignes pour mettre un pivot = 0
	return(B)

def Reduite_max(A):
	B = Gauss_un_max(A)
	for i in range(1,len(A)):
		for j in range(1+i,len(A)-1):
			addition_multiple_ligne(B,-j-1,-i-1,)
