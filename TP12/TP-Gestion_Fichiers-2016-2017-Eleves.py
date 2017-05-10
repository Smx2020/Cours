
#=========================================================
#=========================================================
#
#   TP- 13 -    GESTION de FICHIERS
#
#=========================================================
#=========================================================

""" Enregistrez tous les fichiers du site de colle SANS les ouvrir """
""" Conservez les formats  Format  .csv  ou .txt   """
"""  Enregistrez-les dans le répertoire où vous travaillerez pour ce TP
sous Python """

from Fonction import *

#os.getcwd()   # voir dans quel répertoire vous êtes

#os.chdir('...')  # à complèter avant de valider !

# ... : il faut ici indiquer le chemin pour accéder à VOTRE répertoire
# où vous avez enregistré tous les  fichiers

#os.getcwd()    # vérifiez que vous êtes  dans le bon répertoire




#==============================================================
#
#      Question 1 :  Manipulations sur un fichier
#
#===============================================================


""" Question 1-b """

# Lecture du fichier Test1-2017


#f=open("Test.txt",'r')
#print(f.readline())     # renvoie : la 1ere ligne
#print(f.readline())   # renvoie : la 2eme ligne
#print(f.readline())   # renvoie : la 3eme ligne
#print(f.readline())     # renvoie ''  si vous avez respecté les consignes
# normal  car on était arrivé à la fin !
#f.close()


#f=open("Test.txt",'r')
#1=f.readline()
#L2=f.readline()
#L3=f.readline()
#f.close()

#print(L1 , '\n' , L2 , '\n' , L3)

# la dernière commande renvoie : tout le texte en sautant des lignes

#f=open("Test.txt",'r')
#f.readlines()
# renvoie toutes les lignes

#f.close()

#f=open("Test.txt",'r')
#print(f.readlines())

# renvoie la ligne avec un saut de ligne apres

#f.close()


#f=open("Test.txt",'r')
#L=f.readlines()
#L[0]            # renvoie la ligne 1
#f.close()

#f=open("Test1-2017.txt",'r')
#L=f.readlines()
#print(L[0])            # renvoie la ligne 1
#f.close()

#f=open("Test1-2017.txt",'r')
#Lf=f.readlines()
#for x in Lf :
    #print(x)
#f.close()

# renvoie le texte en sautant des ligne

#f=open("Test.txt",'r')
#print(len(f.readlines()))    # renvoie 3
#f.close()

#f=open("Test.txt",'r')
#Lf=f.readlines()
#Lmots1=[]
#for x in Lf :
    #Lmots1.append(x.split())
#f.close()
#print(Lmots1)

# Lmots renvoie
#[['toto', 'a'], ['test', 'b'], ['tet', 'c']]

""" Question 1-c """

#f=open("Test1.txt",'a')
#f.write('\n' + 'on ajoute une ligne' )   # rajoute une ligne
#f.close()

#f=open("Test1.txt",'r')
#Lf=f.readlines()
#for x in Lf :
    #print(x)
#f.close()

# renvoie : 1 mot par ligne


#f=open("Test1.txt",'a')
#f.write( ' à la fin du fichier ' )		#rajoute  sur la derniere ligne
#f.close()

#f=open("Test1.txt",'r')
#for x in f.readlines() :
    #print(x)
#f.close()

# ATTENTION :  à ce stade , le fichier Test1  a été modifié . Il faut supprimer
# la ligne ajoutée pour revenir au texte initial

#==========================================================
#
#    Question 2 :  Création d'un fichier
#
#==========================================================

#f=open('Test2.txt','w')
#for i in range(2):
    #f.write('ligne numero  %d  \n' %(i+1) )
#f.writelines([ 'ligne numero 3 \n' , 'ligne numero  4 ' ] )
#f.close()

#f=open("Test2.txt",'r')
#for x in f.readlines() :
    #print(x)
#f.close()

# renvoie : toutes les lignes du fichier en sautant des lignes

#f=open("Test2.txt",'r')
#Lf=f.readlines()
#Lmots2=[]
#for x in Lf :
    #Lmots2.append(x.split())
#f.close()
#print(Lmots2)

# renvoie une liste contenants les listes des mots par lignes

#f=open("Test2.txt",'a')
#f.write('\n'+'ligne numero 5')
#f.write('\n'+'ligne numero 6')
#f.close()

# pour vérifier

#f=open("Test2.txt",'r')
#for x in f.readlines() :
    #print(x)
#f.close()


#F1="TP13-Essai-tableau1-Eleves.csv"
#print(F1)
#print(taille(F1)[0])   # rep : 26 c'est juste !
#print(taille(F1)[1])    #  rep : 448   ( je n'ai pas compté )

#T=liste_notes(F1)         #  T=liste_notes(Ftest_OFG)
#for i in range(3):
#    print(T[i])			#Afficher les tableau maths physique Anglais

#Tableau_T=np.array([T[0],T[1],T[2]]).T

#print(moyenne(T[0]))    # renvoie 13.92
#print(moyenne(T[1]))    # renvoie 12.76
#print(moyenne(T[2]))    # renvoie 11.88

#trace_notes(F1)
