import os

def Taille(name):
	f = open(name)
	L = f.readlines()
	S = 0
	for k in range(len(L)):
		for i in range(len(L[k]))
			if L[k][i] != ' ' and L[k][i] != '\n' :
				S = S + 1
	return(k+1,S)
