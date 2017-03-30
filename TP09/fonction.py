simport scipy
from scipy.integrate import odeint
from matplotlib.pyplot as plt

def Euler1(tmin,tmax,F,y0,n):
	"test"
	h = (tmax-tmin)/n
	y = [y0]
	t = [tmin]
	for k in range(n):
		y.append(y[k] + h*F(y[k],t[k]))
		t.append(tmin + h*k)
	return([y,t])

def trace_Euler1(tmin,tmax,F,y0,n):
	L = Euler1(tmin,tmax,F,y0,n)
	solution = odeint(F,y0,L[1])
	Z = solution[:,0]
	plt.plot(L[1],L[0])
	plt.plot(L[1],Z)
	plt.show()
