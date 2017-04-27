import os

def Taille(name):
	f = open(name,'r')
	L = f.readlines()
	S = 0
	for k in range(len(L)):
		for i in range(len(L[k]))
			if L[k][i] != ' ' and L[k][i] != '\n' :
				S = S + 1
	return(k+1,S)

def un_sur_deux(name1,name2):
	f1=open(name1,'r')
	f2=open(name2,'w')
	L = f1.readlines()
	for i in range(0,len(L),2):
		f2.write(L[i])
	f1.close()
	f2.close()

def liste_mots(name):
	f=open(name,'r')
	L = []
