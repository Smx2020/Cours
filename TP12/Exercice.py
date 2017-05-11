from Fonction import *

#print(liste_donnees('TP13-Mouvement-Eleves.csv'))
#trace_mouvement('TP13-Mouvement-Eleves.csv')
#trace_vitesse('TP13-Vitesses-Eleves.csv')

#F1 = 'TP13-valeurs-Eleves.csv'
#f1=open(F1,"r")   # on ouvre le fichier
#i = 0
#for value in csv.reader(f1):
#	i = i + 1
#print(i)

#i = 0
#Lx = []
#Ly = []
#for line in csv.reader(f1):
#	Lx.append(float(line[0]))
#	Ly.append(float(line[1]))
#print(Lx,Ly)

#plt.plot(Lx,Ly,'k*',label='Y en fonction de X')
#plt.show()

#print(trapezes(Lx,Ly))
#print(trapz(Lx,Ly))

F5 = 'TP13-acquisition-Eleves.csv'
f5=open(F5,"r")   # on ouvre le fichier
i = 0
D = []
T = []
TT = []
for line in csv.reader(f5):
	if i :
		D.append(float(line[1]))
		T.append(float(line[0]))
		TT.append(float(line[0])*float(line[0]))
	i = i + 1
print(D)
plt.plot(T,D,'k*',label='D en fonction de T')
plt.plot(TT,D,'k*',label='D en fonction de T*T')
plt.show()
