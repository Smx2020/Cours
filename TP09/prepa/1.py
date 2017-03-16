from scipy import *
from scipy.optimize import *
import numpy

def f(x):
	return(numpy.cos(x)-x)

#print(brentq(f,0,1))	#Donne la valeur de x solution sur [0,1]
#print(fsolve(f,0))		#donne une liste contenant les solutions
#print(root(f,0))
#print(root(f,0).x)		#donne une liste contenant les solutions
