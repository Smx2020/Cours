from Tp import *

#	Exo A-1-1

A = [[1,2,3],[4,0,-1]]

print(len(A),len(A[0]))		#nb de ligne et nb de colonne
print(A[1][0])			#a(2,1)
print(A[1])			#Deuxieme ligne de A
print([A[0][1],A[1][1]])	#Deuxieme colonne de A
print(A[0][2] + A[1][2])	#Somme des coefficient de la 3eme colonne

#	Exo A-1-2

A =[[1,2,3],[4,5,6],[7,8,9] ]

print(trace_matrice(A))
print(matrice_identite(3))
