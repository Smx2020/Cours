import math
import numpy as np

from scipy import inf
from scipy.integrate import quad
from scipy.integrate import trapz
from scipy.integrate import simps

def power(x, n):
	"Renvoie x a la puissance n pour n positif"
	if n == 0:
		return(1)
	else :
		return(x*power(x,n-1))

def carre(x):
	"Renvoie x au carre"
	return(power(x,2))

def fb(x):
	return(1 / (1 + carre(x)))

def fc(x):
	return(1 / (carre(x) + x + 1) )

def fd(x):
	return((carre(x) - 4*x + 5) * math.exp(-x))

def fe(x):
	return(math.exp(-carre(x)))

def FX(a,b,n):
	return(np.linspace(a,b,n))

def FY(g,a,b,n):
	LX = np.linspace(a,b,n)
	return([g(x) for x in LX])
