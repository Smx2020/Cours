from Fonction import *

#print(liste_donnees('TP13-Mouvement-Eleves.csv'))
#trace_mouvement('TP13-Mouvement-Eleves.csv')
#trace_vitesse('TP13-Vitesses-Eleves.csv')

F1 = 'TP13-valeurs-Eleves.csv'
f1=open(F1,"r")   # on ouvre le fichier
#i = 0
#for value in csv.reader(f1):
#	i = i + 1
#print(i)

i = 0
Lx = []
Ly = []
for line in csv.reader(f1):
	Lx.append(float(line[0]))
	Ly.append(float(line[1]))
#print(Lx,Ly)

#plt.plot(Lx,Ly,'k*',label='Y en fonction de X')
#plt.show()

print(trapezes(Lx,Ly))
print(trapz(Lx,Ly))
