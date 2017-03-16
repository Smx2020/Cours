import scipy
import matplotlib.pyplot

def Euler1(tmin,tmax,F,y0,n):
	h = (tmax-tmin)/n
	t = tmin
	y = y0
	for k in range(n+1):
		y = y + h*F(y,t)
		t = t + h
	
