from Fonction import *

n = 1000								#nb de coupure du segment

#############################################	Exercice 0

#print(quad(math.cos,0,math.pi))		#(4.9225526349740854e-17, 2.2102239425853306e-14)
#print(quad(math.exp,-inf,0))			#(1.0000000000000002, 5.842606742906004e-11)
#print(quad(math.exp,-np.inf,0))		#(1.0000000000000002, 5.842606742906004e-11)

#LX =np.linspace(0, math.pi, 101)
#LY = [math.cos(x) for x in LX]
#print(trapz(LX,LY))					#-3.14159265359
#print(simps(LX,LY))					#-3.14159265359

#LX =np.linspace(0, 100, 1001)
#LY = [math.exp(-x) for x in LX]
#print(trapz(LY, LX))					#1.00083319448
#print(simps(LY, LX))					#1.00000055489

#############################################	Exercice 1

#print(quad(carre,0,1))					#0.33333333333333337	1/3
#print(quad(fb,-inf,0))					#1.5707963267948966
#print(quad(fc,1,2))					#0.2195381365438452
#print(quad(fd,0,1))					#2.2642411176571153
#print(quad(fe,0,inf))					#0.8862269254527579

#print(trapz( FX(0,1,n), FY(carre,0,1,n) ))			#0.666666499666
#print(simps( FX(0,1,n), FY(carre,0,1,n) ))			#0.666666666834

#print(trapz( FX(-1000,0,n), FY(fb,-1000,0,n) ))	#-1.57471116546
#print(simps( FX(-1000,0,n), FY(fb,-1000,0,n) ))	#-1.50076037406

#print(trapz( FX(1,2,n), FY(fc,1,2,n) ))			#-0.267157203476
#print(simps( FX(1,2,n), FY(fc,1,2,n) ))			#-0.267157184186

#print(trapz( FX(0,1,n), FY(fd,0,1,n) ))			#-1.52848286394
#print(simps( FX(0,1,n), FY(fd,0,1,n) ))			#-1.52848223606

#print(trapz( FX(0,1000,n), FY(fe,0,1000,n) ))		#-0.8863204291
#print(simps( FX(0,1000,n), FY(fe,0,1000,n) ))		#Erreur
