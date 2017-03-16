import scipy
import matplotlib.pyplot

def Euler1(tmin,tmax,F,y0,n):
	h = (tmax-tmin)/n
	y = [y0]
	t = [tmin]
	for k in range(1,n):
		y.append(y[k] + h*F(y[k],t[k]))
		t.append(tmin + h*k)
	return(y,t)
