import numpy as np
from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def derive(y,x):
	return(a(x)*y(x)+q(x))

x0 = a
xmax = b
numpt = n + 1
X = np.linspace(x0,xmax,numpt)
yo = "valeur"
sol = odeint(derive,y0,X)
Y = sol[:,0]
