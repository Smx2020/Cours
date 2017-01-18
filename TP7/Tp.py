def	check_matrice(M):	#M matrice
	"verifie que la matrice soit rectangulaire"
	comp = len(M[0])
	for i in range(len(M)):
		if len(M[i]) != comp:
			return(True)
	return(False)

def	trace_matrice(M):		#M matrice
	"Calcule la somme des coefficients de la diagonal"
	if check_matrice(M):
		return("Erreur")
	out = 0				#Somme des coeff
	for i in range(len(M)):
		out = out + M[i][i]
	return(out)

def	matrice_identite(n):				#n entier
	"Cree une matrice identite"
	out = [[0 for j in range(n)]for i in range(n)]	#cree la matrice vide
	for i in range(n):
		out[i][i] = 1
	return(out)

