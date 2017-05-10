import os
import csv
import numpy as np
import matplotlib.pyplot as plt

def taille(name):
	f = open(name,'r')
	L = f.readlines()
	S = 0
	for k in range(len(L)):
		for i in range(len(L[k])):
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

def liste_mots(fichier):
    f=open(fichier,'r')   # ouverture en mode lecture
    LM=[]  # initialisation de la liste des mots
    for ligne in f:
          # ligne.split()  est la liste des mots de la ligne
        for mot in ligne.split():
            if mot not in LM:  # si le mot n'est pas encore dans LM
                LM.append(mot)   # on l'ajoute
    f.close()  # on ferme le fichier
    return(LM)

def liste_notes(fichier):    # fichier de type .csv
    M=[]    # notes de maths
    P=[]   # notes de physique
    A=[]   # note d'anglais
    i=0
    f=open(fichier,"r")   # on ouvre le fichier
    lecture=csv.reader(f)
    for ligne in lecture:
        if i!=0:   # on ne tient pas compte de la ligne d'en-tête
        # il faut transformer les chaines de caractères en nombres flottants
            M.append(float(ligne[1]))
            P.append(float(ligne[2]))
            A.append(float(ligne[3]))
        i=i+1
    f.close()    # on referme le fichier
    return(M,P,A)
    #return(np.array(M),np.array(P),np.array(A))

def moyenne(L):
    s=0
    for x in L:
        s=s+x
    return(s/len(L))

def trace_notes(fichier):
    T=liste_notes(fichier)
    Y1=T[0]    # liste des notes de maths ici
    Y2=T[1]   # liste des notes de physique
    Y3=T[2]    # liste des notes d'anglais
    X=np.arange(1,1+len(Y1))
    plt.figure()
    plt.grid(True)
    plt.plot(X,Y1, 'k-',label='maths')
    plt.plot(X,Y2,'r-',label='physique')
    plt.plot(X,Y3,'b-',label='anglais')
    plt.legend(loc='best')
    plt.show()
